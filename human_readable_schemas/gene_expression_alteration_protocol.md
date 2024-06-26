# Expression alteration protocol

- [1. Property `Expression alteration protocol > label`](#label)
- [2. Property `Expression alteration protocol > allele_specific`](#allele_specific)
- [3. Property `Expression alteration protocol > altered_gene_symbols`](#altered_gene_symbols)
  - [3.1. Expression alteration protocol > altered_gene_symbols > altered_gene_symbols items](#autogenerated_heading_2)
- [4. Property `Expression alteration protocol > altered_gene_ids`](#altered_gene_ids)
  - [4.1. Expression alteration protocol > altered_gene_ids > altered_gene_ids items](#autogenerated_heading_3)
- [5. Property `Expression alteration protocol > targeted_genomic_region`](#targeted_genomic_region)
- [6. Property `Expression alteration protocol > expected_alteration_type`](#expected_alteration_type)
- [7. Property `Expression alteration protocol > editing_strategy`](#editing_strategy)
- [8. Property `Expression alteration protocol > method`](#method)
- [9. Property `Expression alteration protocol > altered_locus`](#altered_locus)
  - [9.1. Expression alteration protocol > altered_locus > altered_locus items](#autogenerated_heading_4)
- [10. Property `Expression alteration protocol > guide_sequence`](#guide_sequence)
  - [10.1. Expression alteration protocol > guide_sequence > guide_sequence items](#autogenerated_heading_5)

**Title:** Expression alteration protocol

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the gene expression alteration protocol.

| Property                                                 | Pattern | Type             | Deprecated | Definition | Title/Description                      |
| -------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | -------------------------------------- |
| + [label](#label )                                       | No      | string           | No         | -          | Gene expression alteration protocol ID |
| - [allele_specific](#allele_specific )                   | No      | boolean          | No         | -          | Allele-specific?                       |
| - [altered_gene_symbols](#altered_gene_symbols )         | No      | array of string  | No         | -          | Altered gene symbols                   |
| - [altered_gene_ids](#altered_gene_ids )                 | No      | array of string  | No         | -          | Altered gene IDs                       |
| - [targeted_genomic_region](#targeted_genomic_region )   | No      | enum (of string) | No         | -          | Targeted genomic region                |
| - [expected_alteration_type](#expected_alteration_type ) | No      | enum (of string) | No         | -          | Expected alteration type               |
| - [editing_strategy](#editing_strategy )                 | No      | enum (of string) | No         | -          | Editing strategy                       |
| + [method](#method )                                     | No      | string           | No         | -          | Expression alteration method           |
| + [altered_locus](#altered_locus )                       | No      | array of string  | No         | -          | Altered locus                          |
| - [guide_sequence](#guide_sequence )                     | No      | array of string  | No         | -          | Guide sequence(s)                      |

## <a name="label"></a>1. Property `Expression alteration protocol > label`

**Title:** Gene expression alteration protocol ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique ID for the gene expression alteration protocol.

**Examples:** 

```json
"JAXPE000E_MEIS1"
```

```json
"MSKKI119_MEF2C"
```

| Restrictions                      |                                                                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                    |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22JAXPE000E_MEIS1%22) |

## <a name="allele_specific"></a>2. Property `Expression alteration protocol > allele_specific`

**Title:** Allele-specific?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Indicate if the technique used to modify expression of the gene is allele-specific.

**Examples:** 

```json
false
```

```json
true
```

## <a name="altered_gene_symbols"></a>3. Property `Expression alteration protocol > altered_gene_symbols`

**Title:** Altered gene symbols

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Set of gene(s) whose transcription was modified with this protocol.

**Examples:** 

```json
"MEIS1"
```

```json
"PAX6"
```

```json
"OGG:3000005080"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [altered_gene_symbols items](#altered_gene_symbols_items) | -           |

### <a name="autogenerated_heading_2"></a>3.1. Expression alteration protocol > altered_gene_symbols > altered_gene_symbols items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="altered_gene_ids"></a>4. Property `Expression alteration protocol > altered_gene_ids`

**Title:** Altered gene IDs

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** A set of gene identifier(s) for the genes whose transcription was modified with this protocol. Please use HGNC gene identifiers.

**Examples:** 

```json
"HGNC:7000"
```

```json
"HGNC:6761"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                   | Description |
| ------------------------------------------------- | ----------- |
| [altered_gene_ids items](#altered_gene_ids_items) | -           |

### <a name="autogenerated_heading_3"></a>4.1. Expression alteration protocol > altered_gene_ids > altered_gene_ids items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                           |
| --------------------------------- | ------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                         |
| **Must match regular expression** | ```^HGNC:\d+$``` [Test](https://regex101.com/?regex=%5EHGNC%3A%5Cd%2B%24) |

## <a name="targeted_genomic_region"></a>5. Property `Expression alteration protocol > targeted_genomic_region`

**Title:** Targeted genomic region

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Type of region that is targeted by the gene expression alteration protocol.

**Examples:** 

```json
"full coding region"
```

```json
"exon"
```

Must be one of:
* "exon"
* "intron"
* "promoter"
* "full coding region"
* "other"

## <a name="expected_alteration_type"></a>6. Property `Expression alteration protocol > expected_alteration_type`

**Title:** Expected alteration type

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** How the expression for the gene(s) was altered.

**Examples:** 

```json
"down-regulation"
```

```json
"up-regulation"
```

Must be one of:
* "down-regulation"
* "up-regulation"
* "silencing"

## <a name="editing_strategy"></a>7. Property `Expression alteration protocol > editing_strategy`

**Title:** Editing strategy

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Editing strategy followed in the CRISPR protocol.

**Examples:** 

```json
"full coding length"
```

```json
"critical exon"
```

Must be one of:
* "full coding length"
* "critical exon"
* "termination codon"

## <a name="method"></a>8. Property `Expression alteration protocol > method`

**Title:** Expression alteration method

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Method applied for alteration of the gene expression in the cell line.

**Examples:** 

```json
"CRISPR/Cas9 method"
```

```json
"BAO:0010249"
```

```json
"gene knockdown by lentiviral shRNA transduction"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="altered_locus"></a>9. Property `Expression alteration protocol > altered_locus`

**Title:** Altered locus

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

**Description:** Genomic coordiantes relative to GRCh38 of any genomic alterations made.

**Examples:** 

```json
"chr2:66437727-66464411"
```

```json
"chr5:88751722-88752302"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [altered_locus items](#altered_locus_items) | -           |

### <a name="autogenerated_heading_4"></a>9.1. Expression alteration protocol > altered_locus > altered_locus items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                               |
| **Must match regular expression** | ```^chr\d\d{0,1}:\d+-\d+$``` [Test](https://regex101.com/?regex=%5Echr%5Cd%5Cd%7B0%2C1%7D%3A%5Cd%2B-%5Cd%2B%24) |

## <a name="guide_sequence"></a>10. Property `Expression alteration protocol > guide_sequence`

**Title:** Guide sequence(s)

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Full nucleotide sequence(s) of guide sequences.

**Examples:** 

```json
"AAAGTCGATGTATCTTCTAC"
```

```json
"TTGGTGATAGACGATAGAGAAG"
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
| [guide_sequence items](#guide_sequence_items) | -           |

### <a name="autogenerated_heading_5"></a>10.1. Expression alteration protocol > guide_sequence > guide_sequence items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                         |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Min length**                    | 1                                                                       |
| **Must match regular expression** | ```^[ACGT]+$``` [Test](https://regex101.com/?regex=%5E%5BACGT%5D%2B%24) |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-05-21 at 13:25:13 +0000
