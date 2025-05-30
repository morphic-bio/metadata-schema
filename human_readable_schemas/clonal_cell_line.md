# Clonal cell line

- [1. Property `Clonal cell line > label`](#label)
- [2. Property `Clonal cell line > description`](#description)
- [3. Property `Clonal cell line > distribution`](#distribution)
  - [3.1. Property `Clonal cell line > distribution > internal_project_id`](#distribution_internal_project_id)
  - [3.2. Property `Clonal cell line > distribution > generator_and_vendor`](#distribution_generator_and_vendor)
  - [3.3. Property `Clonal cell line > distribution > date_of_production`](#distribution_date_of_production)
  - [3.4. Property `Clonal cell line > distribution > pipeline_for_generation`](#distribution_pipeline_for_generation)
    - [3.4.1. Clonal cell line > distribution > pipeline_for_generation > pipeline_for_generation items](#autogenerated_heading_2)
  - [3.5. Property `Clonal cell line > distribution > parental_ipsc_line_link`](#distribution_parental_ipsc_line_link)
  - [3.6. Property `Clonal cell line > distribution > sequence_maps`](#distribution_sequence_maps)
  - [3.7. Property `Clonal cell line > distribution > order_enquiry`](#distribution_order_enquiry)
- [4. Property `Clonal cell line > parental_cell_line_name`](#parental_cell_line_name)
- [5. Property `Clonal cell line > clone_id`](#clone_id)
- [6. Property `Clonal cell line > supplier`](#supplier)
- [7. Property `Clonal cell line > type`](#type)
- [8. Property `Clonal cell line > date_established`](#date_established)
  - [8.1. Property `Clonal cell line > date_established > oneOf > item 0`](#date_established_oneOf_i0)
  - [8.2. Property `Clonal cell line > date_established > oneOf > item 1`](#date_established_oneOf_i1)
- [9. Property `Clonal cell line > induction_method`](#induction_method)
- [10. Property `Clonal cell line > culture_environment`](#culture_environment)
- [11. Property `Clonal cell line > culture_medium`](#culture_medium)
- [12. Property `Clonal cell line > drug_treatment`](#drug_treatment)
  - [12.1. Clonal cell line > drug_treatment > drug_treatment items](#autogenerated_heading_3)
- [13. Property `Clonal cell line > zygosity`](#zygosity)
- [14. Property `Clonal cell line > genotyping_accessions`](#genotyping_accessions)
  - [14.1. Clonal cell line > genotyping_accessions > genotyping_accessions items](#autogenerated_heading_4)
- [15. Property `Clonal cell line > cell_line_generation_protocol`](#cell_line_generation_protocol)
- [16. Property `Clonal cell line > treatment_condition`](#treatment_condition)
- [17. Property `Clonal cell line > wt_control_status`](#wt_control_status)

**Title:** Clonal cell line

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the cell line or cell culture biomaterial.

| Property                                                           | Pattern | Type             | Deprecated | Definition | Title/Description             |
| ------------------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------------------- |
| + [label](#label )                                                 | No      | string           | No         | -          | Cell line ID                  |
| - [description](#description )                                     | No      | string           | No         | -          | Cell line description         |
| - [distribution](#distribution )                                   | No      | object           | No         | -          | Distribution                  |
| + [parental_cell_line_name](#parental_cell_line_name )             | No      | string           | No         | -          | Parental cell line name       |
| - [clone_id](#clone_id )                                           | No      | string           | No         | -          | Clone ID                      |
| + [supplier](#supplier )                                           | No      | string           | No         | -          | Cell line supplier            |
| + [type](#type )                                                   | No      | enum (of string) | No         | -          | Cell line type                |
| - [date_established](#date_established )                           | No      | Combination      | No         | -          | Date established              |
| - [induction_method](#induction_method )                           | No      | enum (of string) | No         | -          | Induction method              |
| - [culture_environment](#culture_environment )                     | No      | string           | No         | -          | Culture environment           |
| - [culture_medium](#culture_medium )                               | No      | string           | No         | -          | Culture medium                |
| - [drug_treatment](#drug_treatment )                               | No      | array of string  | No         | -          | Drug treatment                |
| - [zygosity](#zygosity )                                           | No      | enum (of string) | No         | -          | Zygosity                      |
| - [genotyping_accessions](#genotyping_accessions )                 | No      | array of string  | No         | -          | Genotyping accession(s)       |
| - [cell_line_generation_protocol](#cell_line_generation_protocol ) | No      | string           | No         | -          | Cell line generation protocol |
| - [treatment_condition](#treatment_condition )                     | No      | string           | No         | -          | Treatment/Condition           |
| - [wt_control_status](#wt_control_status )                         | No      | enum (of string) | No         | -          | WT/Control status             |

## <a name="label"></a>1. Property `Clonal cell line > label`

**Title:** Cell line ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the cell line. No spaces allowed.

**Examples:** 

```json
"PRMT5_C-terminal_AID_DMSO"
```

```json
"OCM_108_Auxin_24h"
```

| Restrictions                      |                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                                              |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22PRMT5_C-terminal_AID_DMSO%22) |

## <a name="description"></a>2. Property `Clonal cell line > description`

**Title:** Cell line description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the cell line.

**Example:** 

```json
"KOLF2.2J derived knockout cell line, PAX6/STL2 DKO"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="distribution"></a>3. Property `Clonal cell line > distribution`

**Title:** Distribution

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Properties required to the distribution of cell lines

| Property                                                            | Pattern | Type             | Deprecated | Definition | Title/Description                  |
| ------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------------------- |
| + [internal_project_id](#distribution_internal_project_id )         | No      | string           | No         | -          | Internal project ID                |
| + [generator_and_vendor](#distribution_generator_and_vendor )       | No      | enum (of string) | No         | -          | Generator and vendor               |
| + [date_of_production](#distribution_date_of_production )           | No      | string           | No         | -          | Date of production                 |
| - [pipeline_for_generation](#distribution_pipeline_for_generation ) | No      | array of string  | No         | -          | Pipeline for generation            |
| - [parental_ipsc_line_link](#distribution_parental_ipsc_line_link ) | No      | string           | No         | -          | Parental iPSC line repository link |
| - [sequence_maps](#distribution_sequence_maps )                     | No      | string           | No         | -          | Sequence maps                      |
| + [order_enquiry](#distribution_order_enquiry )                     | No      | string           | No         | -          | Order enquiry (email)              |

### <a name="distribution_internal_project_id"></a>3.1. Property `Clonal cell line > distribution > internal_project_id`

**Title:** Internal project ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** Original project ID for which the clone was generated.

**Examples:** 

```json
"MOK20022W"
```

```json
"UM1_H1_1_EOMES_KO"
```

| Restrictions                      |                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                |
| **Must match regular expression** | ```^[a-zA-Z0-9_-]+$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_-%5D%2B%24&testString=%22MOK20022W%22) |

### <a name="distribution_generator_and_vendor"></a>3.2. Property `Clonal cell line > distribution > generator_and_vendor`

**Title:** Generator and vendor

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Generator institute of the clonal cell line.

**Examples:** 

```json
"JAX"
```

```json
"MSK"
```

Must be one of:
* "JAX"
* "MSK"
* "UCSF"
* "NW"

### <a name="distribution_date_of_production"></a>3.3. Property `Clonal cell line > distribution > date_of_production`

**Title:** Date of production

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `date`   |

**Description:** Date of production. Must adhere to ISO 8601 Date and time format standards.

**Examples:** 

```json
"14-07-2023"
```

```json
"27-09-2023"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="distribution_pipeline_for_generation"></a>3.4. Property `Clonal cell line > distribution > pipeline_for_generation`

**Title:** Pipeline for generation

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Established pipeline for generation (if any)

**Examples:** 

```json
"JAX (link/protocols.io)"
```

```json
"Knock in protocol: https://www.sciencedirect.com/science/article/pii/S2666166720300393; Pipeline will be drafted later."
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                              | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [pipeline_for_generation items](#distribution_pipeline_for_generation_items) | -           |

#### <a name="autogenerated_heading_2"></a>3.4.1. Clonal cell line > distribution > pipeline_for_generation > pipeline_for_generation items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="distribution_parental_ipsc_line_link"></a>3.5. Property `Clonal cell line > distribution > parental_ipsc_line_link`

**Title:** Parental iPSC line repository link

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** Link pointing to parental iPSC line characteristics.

**Example:** 

```json
"http://jax.org/ipsc"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="distribution_sequence_maps"></a>3.6. Property `Clonal cell line > distribution > sequence_maps`

**Title:** Sequence maps

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** Link to sequence maps.

**Example:** 

```json
"https://fakeWebsite.com/GCM_KO_allele.gbk"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="distribution_order_enquiry"></a>3.7. Property `Clonal cell line > distribution > order_enquiry`

**Title:** Order enquiry (email)

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `email`  |

**Description:** Order enquiry (email).

**Examples:** 

```json
"enrique@ebi.ac.uk"
```

```json
"enquiryEmail@gmail.com"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="parental_cell_line_name"></a>4. Property `Clonal cell line > parental_cell_line_name`

**Title:** Parental cell line name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A cell line name that references the immediate cell line from which this cell line/clone was derived.

**Examples:** 

```json
"KOLF2.2J"
```

```json
"OCM_108"
```

```json
"ADLI-0-2-011-1-13"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="clone_id"></a>5. Property `Clonal cell line > clone_id`

**Title:** Clone ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A unique ID within the study to identify a clone.

**Example:** 

```json
"kolf2_cloneA"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="supplier"></a>6. Property `Clonal cell line > supplier`

**Title:** Cell line supplier

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The supplier of the cell line.

**Examples:** 

```json
"ATCC"
```

```json
"JAX"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="type"></a>7. Property `Clonal cell line > type`

**Title:** Cell line type

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** The type of cell line.

**Examples:** 

```json
"iPSC"
```

```json
"embryoid"
```

```json
"ESC"
```

Must be one of:
* "iPSC"
* "embryoid"
* "ESC"

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="date_established"></a>8. Property `Clonal cell line > date_established`

**Title:** Date established

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |

**Description:** Date when the cell line was established.

**Examples:** 

```json
"2017-03-19"
```

```json
"2018-11-13T20:20:39+00:00"
```

| One of(Option)                       |
| ------------------------------------ |
| [item 0](#date_established_oneOf_i0) |
| [item 1](#date_established_oneOf_i1) |

### <a name="date_established_oneOf_i0"></a>8.1. Property `Clonal cell line > date_established > oneOf > item 0`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Format**                | `date-time`                                                               |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

### <a name="date_established_oneOf_i1"></a>8.2. Property `Clonal cell line > date_established > oneOf > item 1`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Format**                | `date`                                                                    |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="induction_method"></a>9. Property `Clonal cell line > induction_method`

**Title:** Induction method

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Induction method applied to primary cell culture to induce pluripotent stem cell generation.

**Examples:** 

```json
"Gun particle"
```

```json
"sendai virus"
```

Must be one of:
* "sendai virus"
* "Gun particle"
* "piggyBac transposon"
* "miRNA viral"
* "adenovirus"
* "cre-loxP"
* "plasmid"
* "retroviral"

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="culture_environment"></a>10. Property `Clonal cell line > culture_environment`

**Title:** Culture environment

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Cell culture environment in which cells are grown.

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

## <a name="culture_medium"></a>11. Property `Clonal cell line > culture_medium`

**Title:** Culture medium

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The solid, liquid, or semi-solid medium used to support growth.

**Examples:** 

```json
"RPMI 1640 + 2mM Glutamine + 10-20% FBS"
```

```json
"human placental cord serum"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="drug_treatment"></a>12. Property `Clonal cell line > drug_treatment`

**Title:** Drug treatment

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Drugs added to the growth medium.

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
| **Tuple validation** | See below          |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [drug_treatment items](#drug_treatment_items) | -           |

### <a name="autogenerated_heading_3"></a>12.1. Clonal cell line > drug_treatment > drug_treatment items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="zygosity"></a>13. Property `Clonal cell line > zygosity`

**Title:** Zygosity

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Known zygosity of the gene expression alteration in the cell line

**Examples:** 

```json
"heterozygous"
```

```json
"homozygous"
```

Must be one of:
* "homozygous"
* "heterozygous"
* "mixed"
* "unknown"

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="genotyping_accessions"></a>14. Property `Clonal cell line > genotyping_accessions`

**Title:** Genotyping accession(s)

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** A GenBank assembly accession identifier for the cell line.

**Example:** 

```json
"GCA_000001405.29"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [genotyping_accessions items](#genotyping_accessions_items) | -           |

### <a name="autogenerated_heading_4"></a>14.1. Clonal cell line > genotyping_accessions > genotyping_accessions items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="cell_line_generation_protocol"></a>15. Property `Clonal cell line > cell_line_generation_protocol`

**Title:** Cell line generation protocol

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Protocol for generating any derived cell line for the experiment (if applicable).

**Examples:** 

```json
"DMSO"
```

```json
"IAA"
```

```json
"6 hours"
```

```json
"Auxin_24h"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="treatment_condition"></a>16. Property `Clonal cell line > treatment_condition`

**Title:** Treatment/Condition

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Protocol for generating cell line. e.g. condition or multiple conditions used to generate the cell line (if applicable).

**Examples:** 

```json
"DMSO"
```

```json
"IAA"
```

```json
"6 hours"
```

```json
"Auxin_24h"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="wt_control_status"></a>17. Property `Clonal cell line > wt_control_status`

**Title:** WT/Control status

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Indicate the controls used the experiment (if applicable).

**Examples:** 

```json
"WT"
```

```json
"control"
```

Must be one of:
* "WT"
* "control"

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-29 at 09:57:57 +0000
