# Spreadsheet builder

This small script uses part of the HCA ingest client library to generate a full template out of the stand-alone schema entities in the MorPhiC schema.

The amount of information displayed can be toggled with the "tab_config.yaml", which controls the amount of fields and the structure in the spreadsheet.

## Example usage

```
python3 -o "~/PycharmProjects/metadata-schema/Metadata spreadsheet/builder/test.xlsx" -t "~/PycharmProjects/metadata-schema/Metadata spreadsheet/builder/tab_config.yaml" -s "~/PycharmProjects/metadata-schema/json_schema/type"
```

This will generate a `test.xlsx` file with all the information available in the MorPhiC schema.