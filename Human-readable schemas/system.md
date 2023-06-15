# System
## Common fields
_Fields common to all schemas in this document_

Property name | Description | Type | Required? | Example 
--- | --- | --- | --- | ---
 describedBy | The URL reference to the schema. | string | no |  |  |  | 
schema_version | The version number of the schema in major.minor.patch format. | string | no | 4.6.1

## Provenance
_Provenance information added or generated at time of ingest._

Location: system/1.0.0/provenance

Property name | Description | Type | Required? | Object reference? | User friendly name | Allowed values | Example 
--- | --- | --- | --- | --- | --- | --- | --- 
schema_major_version | The major version number of the schema. | integer | no |  | Schema major version |  | 4; 10
schema_minor_version | The minor version number of the schema. | integer | no |  | Schema minor version |  | 6; 15
submission_date | When project was first submitted to database. | string | yes |  | Submission date |  | 
submitter_id | ID of individual who first submitted project. | string | no |  | Submitter ID |  | 
update_date | When project was last updated. | string | no |  | Update date |  | 
updater_id | ID of individual who last updated project. | string | no |  | Updater ID |  | 
document_id | Identifier for document. | string | yes |  | Document ID |  | 
accession | A unique accession for this entity, provided by the broker. | string | no |  | Accession |  | 

