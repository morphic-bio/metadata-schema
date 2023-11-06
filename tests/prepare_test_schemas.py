import json
import glob
import os


ROOT_PATH = os.path.join(*os.path.abspath(__file__).split("/")[:-2])

import collections.abc

def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def return_schemas_paths(path_to_type_folder):
    schemas = glob.glob(os.path.join(path_to_type_folder, "**", "*.json"), recursive=True)
    return [os.path.join(path_to_type_folder, schema) for schema in schemas]


def solve_allof(schema):
    """
    Loads the system module
    :param schema:
    :return:
    """
    allOf = schema['allOf']
    for subschema in allOf:
        if "$ref" not in subschema:
            continue
        path = f"/{os.path.join(ROOT_PATH, 'json_schema/system/document.json')}"
        with open(path, 'r') as f:
            system = json.load(f)
        # This function updates the restrictions from the system schema
        subschema = update(subschema, system)
    schema['allOf'][0] = subschema
    # Delete redundant info
    del schema['allOf'][0]['$ref']
    del schema['allOf'][0]['$schema']
    del schema['allOf'][0]['definitions']
    return schema

def main(path_to_type_folder):
    schemas = return_schemas_paths(path_to_type_folder)
    for schema_path in schemas:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        schema = solve_allof(schema)
        with open(f"{schema['name']}.json", 'w') as f:
            json.dump(schema, f, indent=4)

if __name__ == '__main__':
    main("/Users/enrique/PycharmProjects/metadata-schema/json_schema/type")