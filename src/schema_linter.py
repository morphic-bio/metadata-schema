import argparse
import json
import logging
import os
import re
import sys
from urllib.error import HTTPError
from urllib.request import urlopen

import requests as requests
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

# Current working directory

cwd = os.getcwd().split("/")[-1]

# Schema fields

# Properties

required_properties = ['describedBy', 'schema_version']

required_ontology_properties = ['text', 'ontology', 'ontology_label']

system_supplied_properties = ['describedBy', 'schema_version', 'schema_type', 'provenance']

# The following properties are exempt from needing examples
# because an example might bias what value a contributor supplies
example_exempt_properties = ['biomaterial_id', 'biomaterial_name', 'biomaterial_description', 'process_id', 'process_name', 'process_description', 'protocol_id', 'protocol_name', 'protocol_description', 'project_description', 'parent', 'sibling', 'child']

# Property attributes

property_attributes = ['description', 'type', 'pattern', 'example', 'enum', '$ref', 'user_friendly', 'items', 'guidelines', 'format', 'comment', 'maximum', 'minimum', 'oneOf']

ontology_attributes = ['graph_restriction', 'ontologies', 'classes', 'relations', 'direct', 'include_self']

graph_restriction_attributes = ['ontologies', 'classes', 'relations', 'direct', 'include_self']

# Accepted environments and conversion for OLS API url

ENVIRONMENTS = ['develop', 'integration', 'staging', 'master']

OLS_ENVIRONMENT = {
    "develop": "dev",
    "integration": "integration",
    "staging": "staging",
    "master": "staging"
}

def argument_parser():
    # Create the parser, define arguments and return it
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', '-e', type=str, dest='environment', help='environment the OLS API feeds on',
                        default='staging', action='store', choices=ENVIRONMENTS)
    return parser


class SchemaLinter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def lintSchema(self, path, ols_api):
        path = os.path.abspath(path)
        schema_filename = path.split("/")[-1].split(".")[0]
        errors = []
        warnings = []
        try:
            schema = self.get_json_from_file(path)
        except Exception as e:
            errors.append(f'{path}: cannot parse json: {str(e)}')
            return warnings, errors
        try:
            json_schema = requests.get(schema['$schema']).json()
            validate(instance=schema, schema=json_schema)
        except KeyError as e:
            errors.append(f'{path}: cannot read $schema dialect reference: {str(e)}')
        except ValidationError as e:
            errors.append(f'{path}: problem validating document: invalid json path \'{e.json_path}\' {str(e)}')
        properties = schema['properties']

        # SCHEMA-LEVEL CHECKS

        # additionalProperties must be set to false
        if "additionalProperties" in schema and schema['additionalProperties'] == True:
            errors.append(path + ": additional properties not allowed.")

        # $schema must be set to draft-07
        if "$schema" in schema and schema['$schema'] != "http://json-schema.org/draft-07/schema#":
            errors.append(path + ": Must have $schema set to http://json-schema.org/draft-07/schema#.")

        # description should be a sentence - start with capital letter and end with full stop
        if 'description' in schema and not re.match('^[A-Z][^?!]*[.]$',schema['description']):
            warnings.append(path + ": The `description` of the schema is not a sentence (" +
                            schema['description'] + ").")

        # Schema filename must match name of the schema in the describedBy URL
        if "describedBy" in schema and properties['describedBy']['pattern'].split("/")[-1] != schema_filename:
            errors.append(path + ": End of `describedBy` URL (" + properties['describedBy'][
                'pattern'].split("/")[-1] + ") must match schema filename (" + schema_filename + ").")

        # Schema filename must match schema name field
        if "name" in schema and schema['name'] != schema_filename:
            errors.append(path +": The `name` attribute (" + schema[
                'name'] + ") must match the schema filename (" + schema_filename + ").")

        # Schema type must be set to object
        if "type" in schema and schema['type'] != "object":
            errors.append(path + ": The `type` attribute must be set to \"object\".")

        # All required fields must actually be in the schema
        if "required" in schema:
            for req_prop in schema["required"]:
                if req_prop not in properties:
                    errors.append("Property `" + req_prop + "` is required in " + path +" but is missing under properties.")

        # Schema titles should be sentence-case (begin with uppercase letter, no underscores)
        if "title" in schema:
            if (not schema['title'][0].isupper()) or ("_" in schema['title']):
                warnings.append(path + ": title \"" +schema['title'] + "\" doesn't start with an uppercase char or contains an underscore.")

        # PROPERTY-LEVEL CHECKS

        # Properties `describedBy` and `schema_version` must be present in each schema
        for ep in required_properties:
            if ep not in properties:
                errors.append(path + ": Missing required property `" + ep + "`.")

        # Properties `text`, `ontology` and `ontology_label` must be present in each ontology schema
        if "ontology" in schema_filename:
            for p in required_ontology_properties:
                if p not in properties:
                    errors.append(path + ": Missing required property `" + p + "`.")

        # All type schemas must have corresponding _core property

        # PER-PROPERTY CHECKS

        for property in properties:

            # Property name must contain only lowercase letters, numbers, and underscores
            # TODO: Should be sys.exit() but currently HDBR_accession field fails this
            # TODO: Fix HDBR_accession field prior to implementing sys.exit()
            if not re.match("^[a-z0-9_]+$", property) and property not in ['describedBy']:
                warnings.append(path + ": Property `" + property + "` contains non-lowercase/underscore characters.")

            # Property must contain description attribute
            if 'description' not in properties[property].keys():
                errors.append(path + ": Keyword `description` missing from property `" + property + "`.")

            # Property must contain user-friendly attribute
            # Currently excludes ingest-supplied fields and links.json
            # TODO: Should apply to provenance fields in Type entities
            # TODO: Add user-friendly to provenance fields prior to removing provenance from list below
            if 'user_friendly' not in properties[property].keys() and property not in ['schema_version', 'schema_type', 'describedBy', 'provenance']:
                if schema_filename not in ['links']:
                    errors.append(path + ": Keyword `user_friendly` missing from property `" + property + "`.")

            # Property must contain type attribute
            if 'type' not in properties[property].keys():
                errors.append(path + ": Keyword `type` missing from property `" + property + "`.")

            else:
                # type attribute must be set to one of the valid JSON types
                if properties[property]['type'] not in ["string", "number", "boolean", "array", "object", "integer"]:
                    errors.append(path + ": Type `" + properties[property]['type'] + "` is not a valid JSON type.")

                # Property of type array must contain the attribute items
                if properties[property]['type'] == "array" and 'items' not in properties[property].keys():
                    errors.append(path + ": Property `" + property + "` is type array but doesn't contain items.")

                # Property of type array must contains the attribute items
                # items must have either type or $ref attribute
                if properties[property]['type'] == "array" and 'items' in properties[property].keys() and '$ref' not in properties[property]['items'].keys() and 'type' not in properties[property]['items'].keys():
                    errors.append(path +": Property `" + property + "` is type array but items attribute doesn't contain type or $ref attribute.")

                # Property of type object must contains the attribute $ref
                if properties[property]['type'] == "object" and '$ref' not in properties[property].keys():
                    errors.append(path +": Property `" + property + "` is type object but doesn't contain $ref.")

            # format must be a valid JSON format
            if 'format' in properties[property].keys() and properties[property]['format'] not in ["date", "date-time", "email"]:
                errors.append(path +": Format `" + properties[property]['format'] + "` is not a valid JSON format).")

            # description should be a sentence - start with capital letter and end with full stop
            if 'description' in properties[property].keys() and not re.match('^[A-Z][^?!]*[.]$', properties[property]['description']):
                warnings.append(path +": The `description` for property `" + property + "` is not a sentence (" + properties[property]['description'] + ").")

            # guidelines should be a sentence
            if 'guidelines' in properties[property].keys() and not re.match('^[A-Z][^?!]*[.]$', properties[property]['guidelines']):
                warnings.append(path +": The `guidelines` for property `" + property + "` is not a sentence (" + properties[property]['guidelines'] + ").")

            # pattern must be a valid regex
            if 'pattern' in properties[property].keys():
                try:
                    re.compile(properties[property]['pattern'])
                    is_valid_regex = True
                except re.error:
                    is_valid_regex = False
                if not is_valid_regex:
                    errors.append(path +": The `pattern` for property `" + property + "` (" + properties[property]['pattern'] + ") is not a valid regex pattern.")

            # example values must match regex pattern
            if 'pattern' in properties[property].keys() and 'example' in properties[property].keys():
                examples = properties[property]['example'].split(";")
                for ex in examples:
                    if not re.match(properties[property]['pattern'], ex.strip()):
                        errors.append(path +": Example " + ex.strip() + " for property `" + property + "` (" +
                                      properties[property]['pattern'] + ") does not match regex pattern " + properties[property]['pattern'] + ".")

            # All $ref referenced schemas must exist
            if '$ref' in properties[property].keys():
                if (schema_path + "/" + properties[property]['$ref']) not in jsons:
                    errors.append(path +": $ref schema (" + properties[property]['$ref'] + ") in property " + property + " does not exist.")

            # Property should contain example attribute
            # Except for system-supplied fields, id/name/description fields, and when importing module ($ref)
            if 'example' not in properties[property].keys() and property not in system_supplied_properties and property not in example_exempt_properties and schema_filename not in ['links', 'provenance']:
                if 'items' in properties[property].keys() and '$ref' not in properties[property]['items'].keys():
                    warnings.append(path +": Keyword `example` missing from property `" + property + "`")
                elif 'items' not in properties[property].keys() and '$ref' not in properties[property].keys():
                    warnings.append(path +": Keyword `example` missing from property `" + property + "`")

            # Property should contain 1 or 2 examples separated by semicolon
            # Excludes enums that list all valid values (Should be one of)
            elif 'example' in properties[property].keys() and property not in system_supplied_properties and schema_filename not in ['links', 'provenance']:
                if not re.match("^Should be one of", str(properties[property]['example'])):
                    ex = str(properties[property]['example']).split(";")
                    if len(ex) == 1 and re.search(",", ex[0]):
                        warnings.append(path +": Property `" + property + "` might have multiple examples that aren't separated by a semicolon (" + str(properties[property]['example']) + ")")

            # _unit properties should have matching property w/o _unit
            if re.match("^[a-z_]+_unit$", property):
                if property.split("_unit")[0] not in properties:
                    warnings.append(path +": Has unit property `" + property + "` but no corresponding `" + property.split("_unit")[0] + "` property")

            # ADDITIONAL PROPERTY CHECKS & SPECIFIC ONTOLOGY CHECKS

            for kw in properties[property].keys():
                # Ontology field must have graph_restriction property that is an object
                if property == 'ontology' and 'graph_restriction' not in properties[property].keys():
                    errors.append(path +": Keyword `graph_restriction` missing from property `" + property + "`.")

                if property == 'ontology' and kw == 'graph_restriction':
                    nested_keywords = properties[property][kw]

                    # graph_restriction property must contain all required attributes
                    for gra in graph_restriction_attributes:
                        if gra not in nested_keywords:
                            errors.append(path +": `graph_restriction` missing a required attribute `" + gra + "`.")

                    for nkw in nested_keywords.keys():

                        # Attributes for graph_restriction must be one of acceptable values
                        if nkw not in ontology_attributes:
                            errors.append(path +": Keyword `" + nkw + "` is not an acceptable graph_restriction keyword property.")

                    # graph_restriction 'direct' attribute must be 'false'
                    if properties['ontology']['graph_restriction']['direct'] is not False:
                        errors.append(path +": Keyword 'direct' must be set to 'false', not " + str(properties['ontology']['graph_restriction']['direct']) + ".")

                    # graph_restriction 'include_self' attribute must be 'false' or 'true'
                    if not isinstance (properties['ontology']['graph_restriction']['include_self'], bool):
                        errors.append(path +": Keyword 'include_self' must be set to 'false' or 'true', not " + str(
                            properties['ontology']['graph_restriction']['include_self']) + ".")

                    # graph_restriction 'relations' attribute must be a list
                    if not isinstance(properties['ontology']['graph_restriction']['relations'], list):
                        errors.append(path +": Keyword 'relations' must be a list.")

                    # graph_restriction 'classes' attribute must be a list
                    if not isinstance(properties['ontology']['graph_restriction']['classes'], list):
                        errors.append(path +": Keyword 'classes' must be a list.")

                    # graph_restriction 'ontologies' attribute must be a list
                    if not isinstance(properties['ontology']['graph_restriction']['ontologies'], list):
                        errors.append(path +": Keyword 'ontologies' must be a list.")

                    # graph_restriction 'relations' must at least contain item "rdfs:subClassOf"
                    if 'rdfs:subClassOf' not in properties['ontology']['graph_restriction']['relations']:
                        errors.append(path +": Keyword 'relations' must contain item 'rdfs:subClassOf'")

                    # graph_restriction 'ontologies' must contain ontologies that are valid within the HCA ontology space
                    # TODO: consider removing ontologies that are not within the HCA namespace and making this an error
                    checked_ontologies = {}
                    for ontology in properties['ontology']['graph_restriction']['ontologies']:
                        if ontology not in checked_ontologies:
                            ols_ontologies_url = ols_api + '/ontologies/' + ontology.replace('obo:','')

                            try:
                                urlopen(ols_ontologies_url)
                                checked_ontologies[ontology] = "pass"
                            except HTTPError as e:
                                warnings.append(schema_filename  + ".json: Ontology " + ontology + " is not a valid ontology in the HCA ontology space")
                                checked_ontologies[ontology] = "fail"
                        else:
                            if checked_ontologies[ontology] == "fail":
                                warnings.append(schema_filename  + ".json: Ontology " + ontology + " is not a valid ontology in the HCA ontology space")

                    #  graph_restrictions 'classes' must contain only ontology classes that are valid in the HCA ontology space
                    for parent_class in properties['ontology']['graph_restriction']['classes']:
                        ols_search_url = ols_api + '/search?q=' + parent_class.replace('obo:', '') + "&exact=true&groupField=true&queryFields=obo_id"

                        json_url = urlopen(ols_search_url)
                        result = json.loads(json_url.read())

                        if "response" in result and "numFound" in result["response"] and result["response"]["numFound"] == 0:
                            errors.append(path +": Class " + parent_class + " is not a valid ontology term in the HCA ontology space")

                # All property attributes must be in the allowed list of property attributes
                elif kw not in property_attributes:
                    errors.append(path +": Keyword `" + kw + "` in property `" + property + "` is not an allowed property.")

                if isinstance(properties[property][kw], dict) and property != 'ontology':
                    for nkw in properties[property][kw].keys():
                        if nkw not in property_attributes:
                            errors.append(path +": Keyword `" + nkw + "` in property `" + property + "` is not an allowed property.")

        return warnings, errors

    def get_json_from_file(self, filename, warn = False):
        """Loads json from a file.
        Optionally specify warn = True to warn, rather than
        fail if file not found."""
        f = open(filename, 'r')
        return json.loads(f.read())


if __name__ == "__main__":
    # Define the environment, transforming 'develop' and 'master' to their respective OLS valid environment to
    # define the proper OLS API URL.
    arguments = argument_parser().parse_args(sys.argv[1:])
    environment = OLS_ENVIRONMENT[arguments.environment]
    ols_api = 'https://ontology.{}.archive.data.humancellatlas.org/api'.format(environment)

    schema_path = '../json_schema' if cwd == 'src' else 'json_schema'
    jsons = [os.path.join(dirpath, f)
                   for dirpath, dirnames, files in os.walk(schema_path)
                   for f in files if f.endswith('.json')]

    linter = SchemaLinter()

    # Exclude top-level JSON files like versions.json and property_migrations.json
    # by including JSON file only if the path contains "core", "module", "system", or "type"
    schemas = [j for j in jsons if any(substring in j for substring in ("core", "module", "system", "type"))]

    print("Linting %d schemas" % len(schemas))

    warnings = []
    errors = []
    for s in schemas:
        if 'versions.json' not in s:
            return_msg = linter.lintSchema(s, ols_api)
            warnings.extend(return_msg[0])
            errors.extend(return_msg[1])

    # Print error and warning messages. If any error is found, exit after printing.
    if errors:
        print("\nThe following errors were found:")
        for error_msg in errors:
            print(error_msg)
        print(f'validated {len(schemas)}. found {len(errors)} error(s), {len(warnings)} warnings(s)')
        sys.exit("\nPlease correct the errors before your code is reviewed.")

    if warnings:
        print("\nLinter finished with the following warnings:")
        for warning_msg in warnings:
            print(warning_msg)
    else:
        print("\nLinter finished with no errors and no warnings.")
