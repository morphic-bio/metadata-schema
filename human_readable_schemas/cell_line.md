# Cell line

- [1. Property `Cell line > culture_environment`](#culture_environment)
- [2. Property `Cell line > culture_medium`](#culture_medium)
- [3. Property `Cell line > date_established`](#date_established)
- [4. Property `Cell line > derived_from_cell_line`](#derived_from_cell_line)
- [5. Property `Cell line > description`](#description)
- [6. Property `Cell line > drug_treatment`](#drug_treatment)
- [7. Property `Cell line > genotyping_accessions`](#genotyping_accessions)
- [8. Property `Cell line > induction_method`](#induction_method)
- [9. Property `Cell line > label`](#label)
- [10. Property `Cell line > supplier`](#supplier)
- [11. Property `Cell line > type`](#type)
- [12. Property `Cell line > zygosity`](#zygosity)

**Title:** Cell line

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the cell line or cell culture biomaterial.

| Property                                             | Pattern | Type             | Deprecated | Definition                                           | Title/Description       |
| ---------------------------------------------------- | ------- | ---------------- | ---------- | ---------------------------------------------------- | ----------------------- |
| - [culture_environment](#culture_environment )       | No      | string           | No         | In #/definitions/non_empty_string                    | Culture environment     |
| - [culture_medium](#culture_medium )                 | No      | string           | No         | Same as [culture_environment](#culture_environment ) | Culture medium          |
| - [date_established](#date_established )             | No      | Combination      | No         | Same as [culture_environment](#culture_environment ) | Date established        |
| + [derived_from_cell_line](#derived_from_cell_line ) | No      | string           | No         | Same as [culture_environment](#culture_environment ) | Derived from cell line  |
| - [description](#description )                       | No      | string           | No         | Same as [culture_environment](#culture_environment ) | Cell line description   |
| - [drug_treatment](#drug_treatment )                 | No      | array            | No         | In #/definitions/non_empty_array                     | Drug treatment          |
| - [genotyping_accessions](#genotyping_accessions )   | No      | array            | No         | Same as [drug_treatment](#drug_treatment )           | Genotyping accession(s) |
| - [induction_method](#induction_method )             | No      | enum (of string) | No         | Same as [culture_environment](#culture_environment ) | Induction method        |
| + [label](#label )                                   | No      | string           | No         | In #/definitions/entity_id                           | Cell line ID            |
| + [supplier](#supplier )                             | No      | string           | No         | Same as [culture_environment](#culture_environment ) | Cell line supplier      |
| + [type](#type )                                     | No      | enum (of string) | No         | Same as [culture_environment](#culture_environment ) | Cell line type          |
| - [zygosity](#zygosity )                             | No      | enum (of string) | No         | Same as [culture_environment](#culture_environment ) | Zygosity                |

## <a name="culture_environment"></a>1. Property `Cell line > culture_environment`

**Title:** Culture environment

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/non_empty_string |

**Description:** Cell culture environment in which cells are grown.

**Examples:** 

```json
"Adherent cell culture"
```

```json
"Suspension cell culture"
```

**Examples:** 

```json
"Adherent cell culture"
```

```json
"Suspension cell culture"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="culture_medium"></a>2. Property `Cell line > culture_medium`

**Title:** Culture medium

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** The solid, liquid, or semi-solid medium used to support growth.

**Examples:** 

```json
"RPMI 1640 + 2mM Glutamine + 10-20% FBS"
```

```json
"human placental cord serum"
```

## <a name="date_established"></a>3. Property `Cell line > date_established`

**Title:** Date established

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `combining`                                 |
| **Required**           | No                                          |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** Date when the cell line was established.

**Examples:** 

```json
"2017-03-19"
```

```json
"2018-11-13T20:20:39+00:00"
```

## <a name="derived_from_cell_line"></a>4. Property `Cell line > derived_from_cell_line`

**Title:** Derived from cell line

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | Yes                                         |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** A cell line name that references the original cell line from which this cell line/clone was derived.

**Examples:** 

```json
"H1"
```

```json
"KOLF2.2J"
```

## <a name="description"></a>5. Property `Cell line > description`

**Title:** Cell line description

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** A general description of the cell line.

**Example:** 

```json
"KOLF2.2J derived knockout cell line, PAX6/STL2 DKO"
```

## <a name="drug_treatment"></a>6. Property `Cell line > drug_treatment`

**Title:** Drug treatment

|                |                               |
| -------------- | ----------------------------- |
| **Type**       | `array`                       |
| **Required**   | No                            |
| **Defined in** | #/definitions/non_empty_array |

**Description:** Drugs added to the growth medium.

**Examples:** 

```json
"100 ug/mL ampicillin"
```

```json
"15 ug/mL tetracycline"
```

**Examples:** 

```json
"100 ug/mL ampicillin"
```

```json
"15 ug/mL tetracycline"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

## <a name="genotyping_accessions"></a>7. Property `Cell line > genotyping_accessions`

**Title:** Genotyping accession(s)

|                        |                                   |
| ---------------------- | --------------------------------- |
| **Type**               | `array`                           |
| **Required**           | No                                |
| **Same definition as** | [drug_treatment](#drug_treatment) |

**Description:** A GenBank assembly accession identifier for the cell line.

**Example:** 

```json
"GCA_000001405.29"
```

## <a name="induction_method"></a>8. Property `Cell line > induction_method`

**Title:** Induction method

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `enum (of string)`                          |
| **Required**           | No                                          |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** Induction method applied to primary cell culture to induce pluripotent stem cell generation.

**Examples:** 

```json
"Gun particle"
```

```json
"sendai virus"
```

## <a name="label"></a>9. Property `Cell line > label`

**Title:** Cell line ID

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | Yes                     |
| **Defined in** | #/definitions/entity_id |

**Description:** A unique label for the cell line.

**Example:** 

```json
"kolf2_2j_knockout_1"
```

**Example:** 

```json
"kolf2_2j_knockout_1"
```

| Restrictions                      |                                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                                        |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22kolf2_2j_knockout_1%22) |

## <a name="supplier"></a>10. Property `Cell line > supplier`

**Title:** Cell line supplier

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | Yes                                         |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** The supplier of the cell line.

**Examples:** 

```json
"ATCC"
```

```json
"JAX"
```

## <a name="type"></a>11. Property `Cell line > type`

**Title:** Cell line type

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `enum (of string)`                          |
| **Required**           | Yes                                         |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** The type of cell line.

**Examples:** 

```json
"immortalized"
```

```json
"primary"
```

## <a name="zygosity"></a>12. Property `Cell line > zygosity`

**Title:** Zygosity

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `enum (of string)`                          |
| **Required**           | No                                          |
| **Same definition as** | [culture_environment](#culture_environment) |

**Description:** Known zygosity of the gene expression alteration in the cell line

**Examples:** 

```json
"hererozygous"
```

```json
"homozygous"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-11-08 at 15:14:06 +0000