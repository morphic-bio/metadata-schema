# Clonal cell line

- [1. Property `Clonal cell line > label`](#label)
- [2. Property `Clonal cell line > description`](#description)
- [3. Property `Clonal cell line > internal_project_id`](#internal_project_id)
- [4. Property `Clonal cell line > generator_and_vendor`](#generator_and_vendor)
- [5. Property `Clonal cell line > pipeline_for_generation`](#pipeline_for_generation)
  - [5.1. Clonal cell line > pipeline_for_generation > pipeline_for_generation items](#autogenerated_heading_2)
- [6. Property `Clonal cell line > date_of_production`](#date_of_production)
- [7. Property `Clonal cell line > parental_ipsc_line`](#parental_ipsc_line)
- [8. Property `Clonal cell line > parental_ipsc_line_link`](#parental_ipsc_line_link)
- [9. Property `Clonal cell line > target_gene`](#target_gene)
- [10. Property `Clonal cell line > hgnc_id`](#hgnc_id)
- [11. Property `Clonal cell line > variation_type`](#variation_type)
- [12. Property `Clonal cell line > coordinates`](#coordinates)
- [13. Property `Clonal cell line > allele_type`](#allele_type)
- [14. Property `Clonal cell line > alteration_size`](#alteration_size)
  - [14.1. Clonal cell line > alteration_size > alteration_size items](#autogenerated_heading_3)
- [15. Property `Clonal cell line > culture_medium`](#culture_medium)
  - [15.1. Clonal cell line > culture_medium > culture_medium items](#autogenerated_heading_4)
- [16. Property `Clonal cell line > nuclease`](#nuclease)
  - [16.1. Clonal cell line > nuclease > nuclease items](#autogenerated_heading_5)
- [17. Property `Clonal cell line > guide_rna`](#guide_rna)
  - [17.1. Property `Clonal cell line > guide_rna > first`](#guide_rna_first)
  - [17.2. Property `Clonal cell line > guide_rna > second`](#guide_rna_second)
- [18. Property `Clonal cell line > ssodn`](#ssodn)
  - [18.1. Property `Clonal cell line > ssodn > first`](#ssodn_first)
  - [18.2. Property `Clonal cell line > ssodn > second`](#ssodn_second)
- [19. Property `Clonal cell line > pcr`](#pcr)
  - [19.1. Clonal cell line > pcr > pcr items](#autogenerated_heading_6)
    - [19.1.1. Property `Clonal cell line > pcr > pcr items > forward_primer`](#pcr_items_forward_primer)
    - [19.1.2. Property `Clonal cell line > pcr > pcr items > reverse_primer`](#pcr_items_reverse_primer)
    - [19.1.3. Property `Clonal cell line > pcr > pcr items > type`](#pcr_items_type)
- [20. Property `Clonal cell line > genotype`](#genotype)
- [21. Property `Clonal cell line > karyotype`](#karyotype)
- [22. Property `Clonal cell line > viability_method`](#viability_method)
- [23. Property `Clonal cell line > viability`](#viability)
- [24. Property `Clonal cell line > mycoplasma`](#mycoplasma)
- [25. Property `Clonal cell line > sequence_maps`](#sequence_maps)
- [26. Property `Clonal cell line > order_enquiry`](#order_enquiry)
- [27. Property `Clonal cell line > donor_plasmid`](#donor_plasmid)
  - [27.1. Property `Clonal cell line > donor_plasmid > first_sequence`](#donor_plasmid_first_sequence)
  - [27.2. Property `Clonal cell line > donor_plasmid > second_sequence`](#donor_plasmid_second_sequence)

**Title:** Clonal cell line

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Registration information about the a clonal cell line.

| Property                                               | Pattern | Type             | Deprecated | Definition | Title/Description                  |
| ------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ---------------------------------- |
| + [label](#label )                                     | No      | string           | No         | -          | Clone ID                           |
| - [description](#description )                         | No      | string           | No         | -          | Cell line description              |
| + [internal_project_id](#internal_project_id )         | No      | string           | No         | -          | Internal project ID                |
| + [generator_and_vendor](#generator_and_vendor )       | No      | enum (of string) | No         | -          | Generator and vendor               |
| - [pipeline_for_generation](#pipeline_for_generation ) | No      | array of string  | No         | -          | Pipeline for generation            |
| + [date_of_production](#date_of_production )           | No      | string           | No         | -          | Date of production                 |
| + [parental_ipsc_line](#parental_ipsc_line )           | No      | string           | No         | -          | Parental iPSC line                 |
| - [parental_ipsc_line_link](#parental_ipsc_line_link ) | No      | string           | No         | -          | Parental iPSC line repository link |
| + [target_gene](#target_gene )                         | No      | string           | No         | -          | Target gene                        |
| + [hgnc_id](#hgnc_id )                                 | No      | string           | No         | -          | HGNC ID                            |
| + [variation_type](#variation_type )                   | No      | string           | No         | -          | Variation type                     |
| + [coordinates](#coordinates )                         | No      | string           | No         | -          | Coordinates (GRCh38)               |
| + [allele_type](#allele_type )                         | No      | enum (of string) | No         | -          | Allele type                        |
| + [alteration_size](#alteration_size )                 | No      | array of integer | No         | -          | Insertion/Deletion size            |
| + [culture_medium](#culture_medium )                   | No      | array of string  | No         | -          | Culture medium                     |
| + [nuclease](#nuclease )                               | No      | array of string  | No         | -          | Nuclease                           |
| + [guide_rna](#guide_rna )                             | No      | object           | No         | -          | -                                  |
| + [ssodn](#ssodn )                                     | No      | object           | No         | -          | -                                  |
| - [pcr](#pcr )                                         | No      | array of object  | No         | -          | -                                  |
| - [genotype](#genotype )                               | No      | string           | No         | -          | Genotype                           |
| - [karyotype](#karyotype )                             | No      | string           | No         | -          | Karyotype                          |
| - [viability_method](#viability_method )               | No      | string           | No         | -          | Viability/Mycoplasma method        |
| + [viability](#viability )                             | No      | string           | No         | -          | Viability                          |
| + [mycoplasma](#mycoplasma )                           | No      | string           | No         | -          | Mycoplasma                         |
| - [sequence_maps](#sequence_maps )                     | No      | string           | No         | -          | Sequence maps                      |
| + [order_enquiry](#order_enquiry )                     | No      | string           | No         | -          | Order enquiry (email)              |
| - [donor_plasmid](#donor_plasmid )                     | No      | object           | No         | -          | -                                  |

## <a name="label"></a>1. Property `Clonal cell line > label`

**Title:** Clone ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the clonal cell line. Must be the same as the MorPhiC identifier. Must contain the name of the project as a prefix.

**Examples:** 

```json
"MOK20022W-C01"
```

```json
"UM1_H1_1_EOMES_KO_#1"
```

| Restrictions                      |                                                                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                |
| **Must match regular expression** | ```^[a-zA-Z0-9_\-\#]+$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5C-%5C%23%5D%2B%24&testString=%22MOK20022W-C01%22) |

## <a name="description"></a>2. Property `Clonal cell line > description`

**Title:** Cell line description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the clonal cell line.

**Example:** 

```json
"KOLF2.2J derived knockout cell line, PAX6/STL2 DKO"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="internal_project_id"></a>3. Property `Clonal cell line > internal_project_id`

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

## <a name="generator_and_vendor"></a>4. Property `Clonal cell line > generator_and_vendor`

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

## <a name="pipeline_for_generation"></a>5. Property `Clonal cell line > pipeline_for_generation`

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

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [pipeline_for_generation items](#pipeline_for_generation_items) | -           |

### <a name="autogenerated_heading_2"></a>5.1. Clonal cell line > pipeline_for_generation > pipeline_for_generation items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="date_of_production"></a>6. Property `Clonal cell line > date_of_production`

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

## <a name="parental_ipsc_line"></a>7. Property `Clonal cell line > parental_ipsc_line`

**Title:** Parental iPSC line

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The parental iPSC line used to generate the clone.

**Example:** 

```json
"KOLF2.2J"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="parental_ipsc_line_link"></a>8. Property `Clonal cell line > parental_ipsc_line_link`

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

## <a name="target_gene"></a>9. Property `Clonal cell line > target_gene`

**Title:** Target gene

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Gene perturbed in the iPSC clone

**Examples:** 

```json
"GCM1"
```

```json
"EOMES"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="hgnc_id"></a>10. Property `Clonal cell line > hgnc_id`

**Title:** HGNC ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** HGNC Identifier of the perturbed gene.

**Examples:** 

```json
"HGNC:4197"
```

```json
"HGNC:3372"
```

| Restrictions                      |                                                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                      |
| **Must match regular expression** | ```^HGNC:\d+$``` [Test](https://regex101.com/?regex=%5EHGNC%3A%5Cd%2B%24&testString=%22HGNC%3A4197%22) |

## <a name="variation_type"></a>11. Property `Clonal cell line > variation_type`

**Title:** Variation type

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Perturbation location in the gene (e.g. KO, PTC, CE).

**Examples:** 

```json
"KO"
```

```json
"Double allele Knock-in"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="coordinates"></a>12. Property `Clonal cell line > coordinates`

**Title:** Coordinates (GRCh38)

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** Genomic coordinates for the variation type (Genome Reference Consortium Human Build 38)

**Examples:** 

```json
"chr6:53127676-53145648"
```

```json
"chr3:27719425-27719444"
```

| Restrictions                      |                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                                 |
| **Must match regular expression** | ```^chr\d{,2}:\d+-\d+$``` [Test](https://regex101.com/?regex=%5Echr%5Cd%7B%2C2%7D%3A%5Cd%2B-%5Cd%2B%24&testString=%22chr6%3A53127676-53145648%22) |

## <a name="allele_type"></a>13. Property `Clonal cell line > allele_type`

**Title:** Allele type

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Whether the allele was deleted or inserted.

**Examples:** 

```json
"deletion"
```

```json
"insertion"
```

Must be one of:
* "deletion"
* "insertion"

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="alteration_size"></a>14. Property `Clonal cell line > alteration_size`

**Title:** Insertion/Deletion size

|              |                    |
| ------------ | ------------------ |
| **Type**     | `array of integer` |
| **Required** | Yes                |

**Description:** Size of the insertion or deletion in nucleotides. Use positive integers for insertions and negative integers for deletion.

**Examples:** 

```json
-17972
```

```json
1664
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [alteration_size items](#alteration_size_items) | -           |

### <a name="autogenerated_heading_3"></a>14.1. Clonal cell line > alteration_size > alteration_size items

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

## <a name="culture_medium"></a>15. Property `Clonal cell line > culture_medium`

**Title:** Culture medium

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

**Description:** Culture medium for the clone.

**Example:** 

```json
"StemFlex"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [culture_medium items](#culture_medium_items) | -           |

### <a name="autogenerated_heading_4"></a>15.1. Clonal cell line > culture_medium > culture_medium items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="nuclease"></a>16. Property `Clonal cell line > nuclease`

**Title:** Nuclease

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

**Description:** Nuclease used to generate the clone.

**Example:** 

```json
"Cas9"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be   | Description |
| --------------------------------- | ----------- |
| [nuclease items](#nuclease_items) | -           |

### <a name="autogenerated_heading_5"></a>16.1. Clonal cell line > nuclease > nuclease items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="guide_rna"></a>17. Property `Clonal cell line > guide_rna`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [first](#guide_rna_first )   | No      | string | No         | -          | Guide RNA 1       |
| - [second](#guide_rna_second ) | No      | string | No         | -          | Guide RNA 2       |

### <a name="guide_rna_first"></a>17.1. Property `Clonal cell line > guide_rna > first`

**Title:** Guide RNA 1

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** Guide RNA 1

**Examples:** 

```json
"TGATAAGGTCAGGCCAGCCA"
```

```json
"TGGTTCCCACTGGATGAGAC"
```

| Restrictions                      |                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                             |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24&testString=%22TGATAAGGTCAGGCCAGCCA%22) |

### <a name="guide_rna_second"></a>17.2. Property `Clonal cell line > guide_rna > second`

**Title:** Guide RNA 2

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** Guide RNA 2

**Example:** 

```json
"TAGTATTTCCACCCTCAGTA"
```

| Restrictions                      |                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                             |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24&testString=%22TAGTATTTCCACCCTCAGTA%22) |

## <a name="ssodn"></a>18. Property `Clonal cell line > ssodn`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [first](#ssodn_first )   | No      | string | No         | -          | ssODN 1           |
| - [second](#ssodn_second ) | No      | string | No         | -          | ssODN 2           |

### <a name="ssodn_first"></a>18.1. Property `Clonal cell line > ssodn > first`

**Title:** ssODN 1

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** ssODN 1

**Example:** 

```json
"ACAAAATTCTCAAGCATTTCTGAGGGGAGTCGAATAGGTGAAAACCTTGHHTAAGGAATGGAAACCTGTCCCGTCTGGGGTGTGAAGTGCCCTCTGCTTT"
```

| Restrictions                      |                                                                                                                                                                                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                                                                             |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24&testString=%22ACAAAATTCTCAAGCATTTCTGAGGGGAGTCGAATAGGTGAAAACCTTGHHTAAGGAATGGAAACCTGTCCCGTCTGGGGTGTGAAGTGCCCTCTGCTTT%22) |

### <a name="ssodn_second"></a>18.2. Property `Clonal cell line > ssodn > second`

**Title:** ssODN 2

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** ssODN 2

**Example:** 

```json
"ACAAAATTCTCAAGCATTTCTGAGGGGAGTCGAATAGGTGAAAACCTTGHHTAAGGAATGGAAACCTGTCCCGTCTGGGGTGTGAAGTGCCCTCTGCTTT"
```

| Restrictions                      |                                                                                                                                                                                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                                                                             |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24&testString=%22ACAAAATTCTCAAGCATTTCTGAGGGGAGTCGAATAGGTGAAAACCTTGHHTAAGGAATGGAAACCTGTCCCGTCTGGGGTGTGAAGTGCCCTCTGCTTT%22) |

## <a name="pcr"></a>19. Property `Clonal cell line > pcr`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [pcr items](#pcr_items)         | -           |

### <a name="autogenerated_heading_6"></a>19.1. Clonal cell line > pcr > pcr items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                       | Pattern | Type   | Deprecated | Definition | Title/Description  |
| ---------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------ |
| - [forward_primer](#pcr_items_forward_primer ) | No      | string | No         | -          | PCR forward primer |
| - [reverse_primer](#pcr_items_reverse_primer ) | No      | string | No         | -          | PCR reverse primer |
| - [type](#pcr_items_type )                     | No      | string | No         | -          | PCR type           |

#### <a name="pcr_items_forward_primer"></a>19.1.1. Property `Clonal cell line > pcr > pcr items > forward_primer`

**Title:** PCR forward primer

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** PCR forward primer sequence.

| Restrictions                      |                                                                         |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Min length**                    | 1                                                                       |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24) |

#### <a name="pcr_items_reverse_primer"></a>19.1.2. Property `Clonal cell line > pcr > pcr items > reverse_primer`

**Title:** PCR reverse primer

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** PCR reverse primer sequence.

| Restrictions                      |                                                                         |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Min length**                    | 1                                                                       |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24) |

#### <a name="pcr_items_type"></a>19.1.3. Property `Clonal cell line > pcr > pcr items > type`

**Title:** PCR type

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Type of PCR performed. If performed to amplify a gene, please indicate name (e.g. Neo, Puro)

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="genotype"></a>20. Property `Clonal cell line > genotype`

**Title:** Genotype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Genotype (HOM, HET, NA).

**Examples:** 

```json
"HOM"
```

```json
"Double allele Knock-in"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="karyotype"></a>21. Property `Clonal cell line > karyotype`

**Title:** Karyotype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Karyotyping information (If available).

**Example:** 

```json
"not done"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="viability_method"></a>22. Property `Clonal cell line > viability_method`

**Title:** Viability/Mycoplasma method

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Viability/Mycoplasma method.

**Examples:** 

```json
"JAX (link/protocols.io)"
```

```json
"https://www.abmgood.com/pcr-mycoplasma-detection-kit-g238.html"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="viability"></a>23. Property `Clonal cell line > viability`

**Title:** Viability

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Viability status.

**Examples:** 

```json
"+++"
```

```json
"not done"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="mycoplasma"></a>24. Property `Clonal cell line > mycoplasma`

**Title:** Mycoplasma

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Mycoplasma.

**Example:** 

```json
"Negative"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="sequence_maps"></a>25. Property `Clonal cell line > sequence_maps`

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

## <a name="order_enquiry"></a>26. Property `Clonal cell line > order_enquiry`

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

## <a name="donor_plasmid"></a>27. Property `Clonal cell line > donor_plasmid`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                             | Pattern | Type   | Deprecated | Definition | Title/Description        |
| ---------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------ |
| - [first_sequence](#donor_plasmid_first_sequence )   | No      | string | No         | -          | Donor plasmid 1 sequence |
| - [second_sequence](#donor_plasmid_second_sequence ) | No      | string | No         | -          | Donor plasmid 2 sequence |

### <a name="donor_plasmid_first_sequence"></a>27.1. Property `Clonal cell line > donor_plasmid > first_sequence`

**Title:** Donor plasmid 1 sequence

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** Donor plasmid 1 sequence.

**Examples:** 

```json
"TGATAAGGTCAGGCCAGCCA"
```

```json
"TGGTTCCCACTGGATGAGAC"
```

| Restrictions                      |                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                             |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24&testString=%22TGATAAGGTCAGGCCAGCCA%22) |

### <a name="donor_plasmid_second_sequence"></a>27.2. Property `Clonal cell line > donor_plasmid > second_sequence`

**Title:** Donor plasmid 2 sequence

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** Donor plasmid 2 sequence.

**Example:** 

```json
"TAGTATTTCCACCCTCAGTA"
```

| Restrictions                      |                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                             |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24&testString=%22TAGTATTTCCACCCTCAGTA%22) |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-06-14 at 16:33:26 +0100