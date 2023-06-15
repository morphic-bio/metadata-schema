import sys
import os
import json
import argparse

import yaml
from hca_ingest.template.tab_config import TabConfig
from hca_ingest.template.schema_template import SchemaTemplate
from hca_ingest.template.vanilla_spreadsheet_builder import VanillaSpreadsheetBuilder



def retrieve_schemas(top_path: str) -> list:
    schemas = []
    for base_path, directories, schema_files in os.walk(top_path):
        if not schema_files:
            continue
        for schema_file in schema_files:
            with open(os.path.join(base_path, schema_file), 'r') as f:
                schemas.append(json.load(f))
    return schemas


def generate_tab_config_dict(schema_docs, generate_tab=False):
    schema_template = SchemaTemplate(json_schema_docs=schema_docs)
    tab_config = schema_template.generate_yaml_representation_of_spreadsheets(tabs_only=False)
    tab_config_dict = yaml.load(tab_config, Loader=yaml.FullLoader)
    return tab_config_dict['tabs']


def main(output_path="", tab_config_path="", generate_tab = False, schema_root_path=''):
    # First we need to gather the schemas. TODO: increase the options to retrieve schemas.
    schemas = retrieve_schemas(schema_root_path)

    # Get a valid SchemaTemplate object: if no tab_config is provided, is generated
    if not tab_config_path:
        tabs = generate_tab_config_dict(schemas, generate_tab)
    else:
        with open(tab_config_path, 'r') as f:
            tabs = yaml.load(f, Loader=yaml.FullLoader)
    tab_config = TabConfig(init=tabs)
    schema_template = SchemaTemplate(json_schema_docs=schemas, tab_config=tab_config)

    # Generate a VanillaSpreadsheetBuilder and build the spreadsheet
    spreadsheet_builder = VanillaSpreadsheetBuilder(output_file=output_path)
    spreadsheet_builder.build(schema_template)
    spreadsheet_builder.save_spreadsheet()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-path', required=True, help='Path for the output spreadsheet. Must end in xlsx')
    parser.add_argument('-t', '--tab-config-path', required=True, help='Path for the tab config file. If not provided, a new one will be generated')
    parser.add_argument('-g', '--generate-tab', action="store_true")
    parser.add_argument('-s', '--schema-root-path', required=True, help='Root path for the schemas to generate spreadsheet')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    parser = parse_args()
    main(parser.output_path, parser.tab_config_path, parser.generate_tab, parser.schema_root_path)