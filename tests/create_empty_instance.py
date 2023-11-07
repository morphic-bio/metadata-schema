import json
import argparse


def define_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--schema', help="Schema to create an empty instance from", type=str)
    parser.add_argument('-o', '--output', help='Output path', type=str)
    return parser


def create_empty_instance_from_schema(schema):
    # System properties
    properties = {key: "" for key in schema['allOf'][0]['properties'].keys()}
    # Content properties
    content = {"content": {prop: "" for prop in schema['properties']['content']['properties'].keys()}}
    properties.update(content)
    return properties


def main(schema_path, output_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    empty_instance = create_empty_instance_from_schema(schema)

    with open(output_path, 'w') as f:
        json.dump(empty_instance, f, indent=4)


if __name__ == '__main__':
    parser = define_parser()
    args = parser.parse_args()
    main(args.schema, args.output)