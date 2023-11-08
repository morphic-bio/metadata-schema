# Study

- [1. Property `Study > label`](#label)
- [2. Property `Study > study_title`](#study_title)
- [3. Property `Study > study_description`](#study_description)
- [4. Property `Study > institute`](#institute)
- [5. Property `Study > contact_first_name`](#contact_first_name)
- [6. Property `Study > contact_surname`](#contact_surname)
- [7. Property `Study > contact_emails`](#contact_emails)
- [8. Property `Study > dracc_data_sharing_date`](#dracc_data_sharing_date)
- [9. Property `Study > biological_sample_types`](#biological_sample_types)
- [10. Property `Study > cell_line_names`](#cell_line_names)
- [11. Property `Study > duo_codes`](#duo_codes)
- [12. Property `Study > model_organ_systems`](#model_organ_systems)
- [13. Property `Study > perturbation_type`](#perturbation_type)
- [14. Property `Study > readout_assay`](#readout_assay)
- [15. Property `Study > sequencing_platforms`](#sequencing_platforms)
- [16. Property `Study > target_genes`](#target_genes)
- [17. Property `Study > supplementary_links`](#supplementary_links)
- [18. Property `Study > other_comments`](#other_comments)

**Title:** Study

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A study entity defines the fields needed for representing a study.

| Property                                               | Pattern | Type             | Deprecated | Definition                                 | Title/Description                 |
| ------------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------------------ | --------------------------------- |
| + [label](#label )                                     | No      | string           | No         | In #/definitions/entity_id                 | Study label                       |
| + [study_title](#study_title )                         | No      | string           | No         | In #/definitions/non_empty_string          | Study title                       |
| + [study_description](#study_description )             | No      | string           | No         | Same as [study_title](#study_title )       | Study description                 |
| + [institute](#institute )                             | No      | enum (of string) | No         | Same as [study_title](#study_title )       | Institute                         |
| + [contact_first_name](#contact_first_name )           | No      | string           | No         | Same as [study_title](#study_title )       | Contact first name                |
| + [contact_surname](#contact_surname )                 | No      | string           | No         | Same as [study_title](#study_title )       | Contact surname                   |
| + [contact_emails](#contact_emails )                   | No      | array            | No         | In #/definitions/non_empty_array           | Contact email(s)                  |
| - [dracc_data_sharing_date](#dracc_data_sharing_date ) | No      | string           | No         | Same as [study_title](#study_title )       | Estimated DRACC data release date |
| + [biological_sample_types](#biological_sample_types ) | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Biological sample type(s)         |
| + [cell_line_names](#cell_line_names )                 | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Cell line name                    |
| + [duo_codes](#duo_codes )                             | No      | array            | No         | Same as [contact_emails](#contact_emails ) | DUO label(s)                      |
| - [model_organ_systems](#model_organ_systems )         | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Model system(s)                   |
| + [perturbation_type](#perturbation_type )             | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Perturbation type(s)              |
| + [readout_assay](#readout_assay )                     | No      | string           | No         | Same as [study_title](#study_title )       | Readout assay                     |
| + [sequencing_platforms](#sequencing_platforms )       | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Sequencing platform(s)            |
| + [target_genes](#target_genes )                       | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Target gene(s)                    |
| - [supplementary_links](#supplementary_links )         | No      | array            | No         | Same as [contact_emails](#contact_emails ) | Supplementary link(s)             |
| - [other_comments](#other_comments )                   | No      | string           | No         | Same as [study_title](#study_title )       | Other comments                    |

## <a name="label"></a>1. Property `Study > label`

**Title:** Study label

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | Yes                     |
| **Defined in** | #/definitions/entity_id |

**Description:** A short label for the study. It should have no spaces and should be fewer than 50 characters.

**Examples:** 

```json
"CoolOrganStudy"
```

```json
"PAX2KOLFStudy"
```

**Examples:** 

```json
"CoolOrganStudy"
```

```json
"PAX2KOLFStudy"
```

| Restrictions                      |                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                   |
| **Max length**                    | 50                                                                                                                  |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22CoolOrganStudy%22) |

## <a name="study_title"></a>2. Property `Study > study_title`

**Title:** Study title

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | Yes                            |
| **Defined in** | #/definitions/non_empty_string |

**Description:** An official title for the study. Should be fewer than 30 words.

**Examples:** 

```json
"Study of single cells in the human body."
```

```json
"Study of the effect of PAX2 in the KOLF2.2J cell line."
```

**Examples:** 

```json
"Study of single cells in the human body."
```

```json
"Study of the effect of PAX2 in the KOLF2.2J cell line."
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |
| **Max length** | 150 |

## <a name="study_description"></a>3. Property `Study > study_description`

**Title:** Study description

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `string`                    |
| **Required**           | Yes                         |
| **Same definition as** | [study_title](#study_title) |

**Description:** A longer description of the study which includes research goals and experimental approach.

**Example:** 

```json
"A longer description with highlights of your experiment goes here, up to 300 words."
```

## <a name="institute"></a>4. Property `Study > institute`

**Title:** Institute

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | Yes                         |
| **Same definition as** | [study_title](#study_title) |

**Description:** Institute associated with the registered study.

**Examples:** 

```json
"JAX"
```

```json
"MSK"
```

## <a name="contact_first_name"></a>5. Property `Study > contact_first_name`

**Title:** Contact first name

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `string`                    |
| **Required**           | Yes                         |
| **Same definition as** | [study_title](#study_title) |

**Description:** First name of the main person to contact for queries about this study.

**Examples:** 

```json
"Anu"
```

```json
"Enrique"
```

```json
"Wei"
```

## <a name="contact_surname"></a>6. Property `Study > contact_surname`

**Title:** Contact surname

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `string`                    |
| **Required**           | Yes                         |
| **Same definition as** | [study_title](#study_title) |

**Description:** Surname of the main person to contact for queries about this study.

**Examples:** 

```json
"Koci"
```

```json
"Zucchi"
```

## <a name="contact_emails"></a>7. Property `Study > contact_emails`

**Title:** Contact email(s)

|                |                               |
| -------------- | ----------------------------- |
| **Type**       | `array`                       |
| **Required**   | Yes                           |
| **Defined in** | #/definitions/non_empty_array |

**Description:** Email of the person/people to contact for queries about this study.

**Examples:** 

```json
"anotherfakemail@med.miami.edu"
```

```json
"fakemail@ebi.ac.uk"
```

**Examples:** 

```json
"anotherfakemail@med.miami.edu"
```

```json
"fakemail@ebi.ac.uk"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

## <a name="dracc_data_sharing_date"></a>8. Property `Study > dracc_data_sharing_date`

**Title:** Estimated DRACC data release date

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `string`                    |
| **Required**           | No                          |
| **Format**             | `date`                      |
| **Same definition as** | [study_title](#study_title) |

**Description:** Estimated date of data release to the DRACC.

**Examples:** 

```json
"2018-11-13"
```

```json
"2019-11-13"
```

## <a name="biological_sample_types"></a>9. Property `Study > biological_sample_types`

**Title:** Biological sample type(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | Yes                               |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** Does the study contain data extracted from cell lines, organoids and/or embryoid bodies?

**Examples:** 

```json
"cell line"
```

```json
"embryoid body"
```

```json
"organoid"
```

## <a name="cell_line_names"></a>10. Property `Study > cell_line_names`

**Title:** Cell line name

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | Yes                               |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** Name of the cell lines used for this study.

**Example:** 

```json
"KOLF2.2J"
```

## <a name="duo_codes"></a>11. Property `Study > duo_codes`

**Title:** DUO label(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | Yes                               |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** Data Usage Ontology code(s) that describe the data sharing restrictions for this study.

## <a name="model_organ_systems"></a>12. Property `Study > model_organ_systems`

**Title:** Model system(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | No                                |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** Model organ system(s) being studied or modelled in this study.

## <a name="perturbation_type"></a>13. Property `Study > perturbation_type`

**Title:** Perturbation type(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | Yes                               |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** Type of perturbation introduced by the gene expression alteration assay.

**Examples:** 

```json
"irreversible gene knockout"
```

```json
"reversible gene knockdown"
```

## <a name="readout_assay"></a>14. Property `Study > readout_assay`

**Title:** Readout assay

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `string`                    |
| **Required**           | Yes                         |
| **Same definition as** | [study_title](#study_title) |

**Description:** High throughput readout assay used in the generation of the study.

**Examples:** 

```json
"EFO:0008931"
```

```json
"EFO:0009310"
```

## <a name="sequencing_platforms"></a>15. Property `Study > sequencing_platforms`

**Title:** Sequencing platform(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | Yes                               |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** Sequencing platform(s) being used to sequence the samples.

## <a name="target_genes"></a>16. Property `Study > target_genes`

**Title:** Target gene(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | Yes                               |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** List of target gene(s) for this study.

**Examples:** 

```json
"PAX2"
```

```json
"PAX6"
```

## <a name="supplementary_links"></a>17. Property `Study > supplementary_links`

**Title:** Supplementary link(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | No                                |
| **Same definition as** | [contact_emails](#contact_emails) |

**Description:** External link(s) pointing to code, supplementary data files, or analysis files associated with the study which will not be uploaded.

**Examples:** 

```json
"http://celltag.org/"
```

```json
"https://github.com/czbiohub/tabula-muris"
```

## <a name="other_comments"></a>18. Property `Study > other_comments`

**Title:** Other comments

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `string`                    |
| **Required**           | No                          |
| **Same definition as** | [study_title](#study_title) |

**Description:** Other comments from the contributor regarding this study.

**Examples:** 

```json
"This study is in early access and is yet to be peer-reviewed"
```

```json
"This study was conducted under very specific conditions and may not apply to all ex vivo cases"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-11-08 at 15:14:06 +0000
