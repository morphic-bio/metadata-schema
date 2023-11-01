import argparse
import json
import sys

ROOT_PROPERTIES_IN_ORDER = ["$schema",
                            "type",
                            "$ref",
                            "format",
                            "pattern",
                            "minLength",
                            "maxLength",
                            "minItems",
                            "description",
                            "$comment",
                            "unevaluatedProperties",
                            "title",
                            "name",
                            "required",
                            "dependentRequired",
                            "allOf",
                            "oneOf",
                            "anyOf",
                            "enum",
                            "properties",
                            "uniqueItems",
                            "graphRestriction",
                            "items",
                            "const",
                            "default",
                            "definitions",
                            "isValidIdentifier",
                            "examples",
                            "prefix",
                            "ontologies",
                            "classes",
                            "relations",
                            "direct",
                            "includeSelf",
                            "queryFields"]

def define_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--json-path", help="Path where the JSON to format is stored", action="store",
                        required=True)
    parser.add_argument("-o", "--output-path", help="Path where the formatted JSON should be stored", action="store",
                        required=False)
    return parser


def sort_schema(schema):
    return dict(sorted(schema.items()))

def find_key_and_apply_function(key, schema, function):
    """
    Recursively traverse a json dictionary and apply a function. Function must have as only argument the schema.
    :param key:
    :param schema:
    :param function:
    :return:
    """
    if isinstance(schema, dict):
        if key in schema:
            schema[key] = function(schema[key])
        for k, v in schema.items():
            schema[k] = find_key_and_apply_function(key, v, function)
    elif isinstance(schema, list):
        for i in range(len(schema)):
            schema[i] = find_key_and_apply_function(key, schema[i], function)
    return schema


def traverse_and_apply_function(schema, function, skip_level=False):
    """
    Recursively traverse a json dictionary and apply a function. Function must have as only argument the schema.
    :param key:
    :param schema:
    :param function:
    :return:
    """
    if isinstance(schema, dict):
        if not skip_level:
            schema = function(schema)
        skip_level = False
        for k, v in schema.items():
            # Probably should add a "ignore_levels" feature
            if k == 'properties' or k == 'dependentRequired':
                skip_level = True
            schema[k] = traverse_and_apply_function(v, function, skip_level)
    elif isinstance(schema, list):
        for i in range(len(schema)):
            schema[i] = traverse_and_apply_function(schema[i], function)
    return schema

def check_arguments(args):
    open(args.json_path, 'r').close()


def sort_root_values(schema):
    ordered_schema = {}
    for key in ROOT_PROPERTIES_IN_ORDER:
        if key in schema:
            ordered_schema[key] = schema[key]
    if any([key not in ROOT_PROPERTIES_IN_ORDER for key in schema.keys()]):
        not_in_keys = [key for key in schema.keys() if key not in ROOT_PROPERTIES_IN_ORDER]
        for key in not_in_keys:
            ordered_schema.update({key: schema[key]})
        print(f"Keys missing!: {not_in_keys}")
    return ordered_schema


def sort_list(l):
    return sorted(l)


def main(json_path, output_path):
    with open(json_path, 'r') as f:
        schema = json.load(f)

    # Sort root values of the whole document (Definitions)
    schema = traverse_and_apply_function(schema, sort_root_values)

    # Sort all fields under 'properties' alphabetically
    schema = find_key_and_apply_function('properties', schema, sort_schema)

    # sort all required properties
    schema = find_key_and_apply_function('required', schema, sort_list)

    # sort all examples
    schema = find_key_and_apply_function('examples', schema, sort_list)

    with open(output_path, 'w') as f:
        json.dump(schema, f, indent=4)



if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    try:
        check_arguments(args)
    except Exception as e:
        sys.exit(f"Error during argument parsing: \n{e}")

    main(args.json_path, args.output_path)