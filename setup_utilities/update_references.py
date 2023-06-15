import os
import json


def describedby_replacement(schema_path):
    path_describedby = schema_path.split('/json_schema')[1]
    new = f"https://raw.githubusercontent.com/morphic-bio/metadata-schema/main/json_schema{path_describedby}"
    return new

def refs_to_hyperlink(schema_content):
    if not isinstance(schema_content, dict):
        return schema_content
    for key, value in schema_content.items():

        if key == "$ref":
            value = value.split('json_schema/')[-1]
            value = value.split('/')  # Add version. TODO: improve versioning
            value = [v for v in value if v != '1.0.0']
            value.insert(-1, '1.0.0')
            value = "/".join(value).replace(".json", "")
            schema_content[key] = f"https://raw.githubusercontent.com/morphic-bio/metadata-schema/main/json_schema/{value}"
        elif isinstance(value, dict):
            schema_content[key] = refs_to_hyperlink(schema_content[key])
    return schema_content


def update_references(schema_path):
    with open(schema_path, 'r') as f:
        schema_content = json.load(f)
    schema_content['properties']['describedBy']['pattern'] = describedby_replacement(schema_path)
    schema_content['$id'] = describedby_replacement(schema_path)
    schema_content['properties'] = refs_to_hyperlink(schema_content['properties'])
    with open(schema_path, 'w') as f:
        json.dump(schema_content, f, indent=4, separators=(', ', ': '))




def main():
    cwd = os.getcwd()
    schemas_dir = f"{'../' if 'setup_utilities' in cwd else ''}json_schema"
    for base_path, directories, files in os.walk(schemas_dir):
        if directories:
            continue  # Only leaf directories
        for file in files:
            update_references(f"{base_path}/{file}")


if __name__ == '__main__':
    main()