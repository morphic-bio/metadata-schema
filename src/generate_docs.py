from json_schema_for_humans.generate import generate_from_schema
from json_schema_for_humans.generation_configuration import GenerationConfiguration

import json
import argparse
import os
import glob
from copy import deepcopy


def define_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema-path', '-s', help='Path to schema(s). Can be a schema or a folder containing schemas', type=str)
    parser.add_argument('--output-path', '-o', help='Output path to store readable schema(s). Will be named as original schema.', type=str, required=False)
    return parser


def retrieve_schemas(schema_path):
    pre_loaded_schemas = {}

    if os.path.isfile(schema_path):
        paths = [schema_path]
    else:
        paths = glob.glob(os.path.join(schema_path, "**", "*.json"), recursive=True)

    for path in paths:
        with open(path, 'r') as f:
            schema = json.load(f)
            del schema['allOf']
            schema['required'] = schema['properties']['content'].get('required', [])
            schema['properties'] = schema['properties']['content']['properties']
        pre_loaded_schemas[os.path.abspath(path)] = deepcopy(schema)
    return pre_loaded_schemas


def main(schema_path, output_path):
    config = GenerationConfiguration(copy_css=False, expand_buttons=True, template_name='md')
    pre_loaded_schemas = retrieve_schemas(schema_path)
    for key, value in pre_loaded_schemas.items():
        schema_name = value['name']
        md = generate_from_schema(key, loaded_schemas=pre_loaded_schemas, config=config)
        with open(f"{os.path.join(output_path, schema_name)}.md", 'w') as f:
            f.write(md)

if __name__ == '__main__':
    parser = define_parser()
    args = parser.parse_args()
    main(args.schema_path, args.output_path)