## Changelog

In this folder, there is a file named `changelog.json`. This file collects all the changes made to the JSON schemas.
There is a JSON schema defining how the file is structured, under system/changelog.json. The main structure and goals
of each part are:

```json
{
  "<schema_path>": {
    "current": "<current_version_of_schema>",
    "changes": [
      {
        "from": "<previous published schema version>",
        "to": "<Published schema version from which these changes are applicable>",
        "minor": "<null||array. null if no changes of this type; array if changes. See 'major'>",
        "major": [
          {
            "addition": "<null||object>. null if no change of this type. see 'update'",
            "deletion": "<null||object>. null if no change of this type. see 'update'",
            "update": {
              "field": ["<field_name>", "<additional path(e.g. 'title', 'examples', 'items')>"],
              "type": "<name||value. `name` updates the property `field` points to; `value` updates the value of that property>",
              "new_value": "<new_value>"
            }
          }
        ]
      }
    ]
  }
}

```
* Any element of the structure above that is enclosed by `<>` is variable. Any element not enclosed is fixed.
* Each element of the `changes` array:
  * Is an `object` with the following keys: `from`, `to`, `minor`, `major` (Skipping patch - Not needed to migrate a document)
  * Represents a **published schema**, meaning you can apply each change separately to get to a specific schema version
  * For `patch` changes, `minor` and `major` fields are left as null. It seems redundant, but when building a story to update a document from
    e.g. 1.1.0 to 2.5.2, you need to collect all versions to be able to correctly parse the `changes` array.
* This document does not fully collect how the schema itself evolves, but rather focuses how documents need to evolve.
  Difficult cases such as adding required fields are not explicitly collected, but rather implied from the fact that
  they are catalogued as additions in a `major` update.

### Migration tips

1. Only major changes are needed to migrate a document. You can ignore `patch` and `minor`, as these are just flavours
   to increase the amount of metadata collected. `minor` and `patch` update collection may be important for non-validation
   services (e.g. a `spreadsheet generator`)
2. `update` changes are, _technically_, always automatically applicable. For changes that are not (e.g. substituting a
   field for another one that is drastically different with different values, etc), please apply a `deletion` and 
   `addition` operation 