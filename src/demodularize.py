import json
from os import walk
from os.path import join


PROPERTIES_TO_IGNORE = ["describedBy", "schema_type", "schema_version", "description", "$ref", "document_id", "ontology_label"]

# Utility functions


def find_type_schemas(path: str) -> list:
    schemas_path = []
    for full_path, subdirectories, files in walk(path):
        if subdirectories:
            continue
        if "type" not in full_path:
            continue
        for file in files:
            if "_1" in file:
                continue
            schemas_path.append(join(full_path, file))

    return schemas_path


def yield_properties(subschema: dict) -> dict:
    prefix = ""
    if "ontology" in subschema['properties']:
        prefix = f"{subschema['name'].replace('_ontology','')}_"
    for property, value in subschema['properties'].items():
        if property not in PROPERTIES_TO_IGNORE:
            yield {f"{prefix}{property}": value}

def load_subschema(ref: str) -> dict:
    try:
        with open(f"/Users/enrique/PycharmProjects/metadata-schema/json_schema/{ref}", "r") as f:
            subschema = json.load(f)
    except:
        return {}
    return subschema

def delete_ignored_properties_from_required(schema):
    schema['required'] = [property for property in schema.get('required') if property not in PROPERTIES_TO_IGNORE]
    return schema


def demodularize_schema(schema):
    """
    Things this function does:
        - If references are a single item, load them in the main properties
        - If references are an array of items, load them as an object (still nested, but there's no way to ensure same length of array properties)
        - Delete ignored properties. List above
        - Move required to main body, unless array of items
    :param schema:
    :return:
    """
    subschema = {}
    for property in list(schema.get('properties', {}).keys()):
        is_ref = False
        is_array = False
        if "items" in schema['properties'][property]:
            is_array = True
            if "$ref" in schema['properties'][property]['items']:
                is_ref = True
                subschema = load_subschema(schema['properties'][property]['items']['$ref'])
                for property_to_del in PROPERTIES_TO_IGNORE:
                    if property_to_del in schema['properties'][property]['items']:
                        del schema['properties'][property]['items'][property_to_del]
                subschema = demodularize_schema(subschema)
        elif "$ref" in schema['properties'][property]:
            is_ref = True
            subschema = load_subschema(schema['properties'][property]['$ref'])
            for property_to_del in PROPERTIES_TO_IGNORE:
                if property_to_del in schema['properties'][property]:
                    del schema['properties'][property][property_to_del]
            subschema = demodularize_schema(subschema)
        if not subschema:
            continue
        if is_ref:
            if is_array:
                schema['properties'][property]['items']['properties'] = {}
                if 'required' in subschema:
                    schema['properties'][property]['items']['required'] = subschema['required']
            for new_property in yield_properties(subschema):
                if is_array:
                    schema['properties'][property]['items']['properties'].update(new_property)
                else:
                    schema['properties'].update(new_property)
            else:
                if not is_array:
                    del schema['properties'][property]

        # Add required properties
        if is_ref and not is_array:
            if not schema.get('required') and subschema.get('required'):
                schema['required'] = []
            schema['required'].extend([prop for prop in subschema.get('required', []) if prop not in PROPERTIES_TO_IGNORE])

    return schema


def schema_to_latest(schema):
    schema['$schema'] = "https://json-schema.org/draft/2020-12/schema"
    return schema

def delete_id(schema):
    if schema.get('$id'):
        del schema['$id']
    return schema



def save_schema(schema, path):
    with open(path, "w") as f:
        schema['properties'] = dict(sorted(schema['properties'].items()))
        json.dump(schema, f, indent=4)


"""
List of updates:
- Delete ignored properties from required
- Demodularization of all the loaded schemas. Aside from the script, this requires manual intervention for ontology modules (Can't have properties named "text", "ontology")
    - Also core properties should be renamed to specific entity
- All schemas to latest draft
- "$id" out

    


LIST OF IMPROVEMENTS
- Add a keyword in ontologies that points out to repository to suggest new term
"""
def main(path):
    type_schemas_path = find_type_schemas(path)
    for schema_path in type_schemas_path:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        schema = delete_ignored_properties_from_required(schema)
        demodularized_schema = demodularize_schema(schema)
        demodularized_schema = delete_id(demodularized_schema)
        demodularized_schema = schema_to_latest(demodularized_schema)
        demodularized_schema = schema
        save_schema(demodularized_schema, f"{schema_path}_1.json")

if __name__ == "__main__":
    main("/Users/enrique/PycharmProjects/metadata-schema/json_schema")