# Library preparation

- [1. Property `Library preparation > label`](#label)
- [2. Property `Library preparation > description`](#description)
- [3. Property `Library preparation > library_preparation_protocol_id`](#library_preparation_protocol_id)
- [4. Property `Library preparation > average_fragment_size`](#average_fragment_size)
- [5. Property `Library preparation > input_amount_value`](#input_amount_value)
- [6. Property `Library preparation > input_amount_unit`](#input_amount_unit)
- [7. Property `Library preparation > concentration_value`](#concentration_value)
- [8. Property `Library preparation > concentration_unit`](#concentration_unit)
- [9. Property `Library preparation > total_yield_value`](#total_yield_value)
- [10. Property `Library preparation > total_yield_unit`](#total_yield_unit)
- [11. Property `Library preparation > cdna_pcr_cycles`](#cdna_pcr_cycles)
- [12. Property `Library preparation > pcr_cycles_for_indexing`](#pcr_cycles_for_indexing)

**Title:** Library preparation

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the library preparation.

| Property                                                               | Pattern | Type    | Deprecated | Definition | Title/Description                          |
| ---------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------------------ |
| + [label](#label )                                                     | No      | string  | No         | -          | Library preparation ID                     |
| - [description](#description )                                         | No      | string  | No         | -          | Library preparation description            |
| + [library_preparation_protocol_id](#library_preparation_protocol_id ) | No      | string  | No         | -          | Library preparation protocol ID            |
| - [average_fragment_size](#average_fragment_size )                     | No      | integer | No         | -          | Average fragment size                      |
| - [input_amount_value](#input_amount_value )                           | No      | number  | No         | -          | Library input amount value                 |
| - [input_amount_unit](#input_amount_unit )                             | No      | string  | No         | -          | Library input amount unit                  |
| - [concentration_value](#concentration_value )                         | No      | number  | No         | -          | Library concentration value                |
| - [concentration_unit](#concentration_unit )                           | No      | string  | No         | -          | Library concentration unit                 |
| - [total_yield_value](#total_yield_value )                             | No      | number  | No         | -          | Library final yield value                  |
| - [total_yield_unit](#total_yield_unit )                               | No      | string  | No         | -          | Library final yield unit                   |
| - [cdna_pcr_cycles](#cdna_pcr_cycles )                                 | No      | integer | No         | -          | Number of iterations of cDNA amplification |
| - [pcr_cycles_for_indexing](#pcr_cycles_for_indexing )                 | No      | integer | No         | -          | Number of PCR cycles for indexing          |

## <a name="label"></a>1. Property `Library preparation > label`

**Title:** Library preparation ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the library preparation. No spaces allowed.

**Example:** 

```json
"kolf2_2j_knockout_1_trophoblast_library_preparation1S"
```

| Restrictions                      |                                                                                                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                                          |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22kolf2_2j_knockout_1_trophoblast_library_preparation1S%22) |

## <a name="description"></a>2. Property `Library preparation > description`

**Title:** Library preparation description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the library preparation.

**Example:** 

```json
"Run 1, batch 1S, library preparation from KOLF2.2J derived trophoblasts"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="library_preparation_protocol_id"></a>3. Property `Library preparation > library_preparation_protocol_id`

**Title:** Library preparation protocol ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** An ID for the library preparation protocol used. No spaces allowed.

**Examples:** 

```json
"msk_pooled_wt_transcriptome"
```

```json
"Library_preparation_bulk.pdf"
```

```json
"JAXPL001"
```

| Restrictions                      |                                                                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22msk_pooled_wt_transcriptome%22) |

## <a name="average_fragment_size"></a>4. Property `Library preparation > average_fragment_size`

**Title:** Average fragment size

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Average fragment size for the transcripts in the library preparation, in base pairs.

**Examples:** 

```json
150
```

```json
256
```

```json
450
```

## <a name="input_amount_value"></a>5. Property `Library preparation > input_amount_value`

**Title:** Library input amount value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Volume or mass of nucleic acid material used as input to library generation.

**Examples:** 

```json
7.5
```

```json
8
```

```json
9.1
```

```json
300
```

## <a name="input_amount_unit"></a>6. Property `Library preparation > input_amount_unit`

**Title:** Library input amount unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unit by which the value of the library input was measured.

**Examples:** 

```json
"UO:0000101"
```

```json
"microliter"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="concentration_value"></a>7. Property `Library preparation > concentration_value`

**Title:** Library concentration value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Final concentration of the library.

**Examples:** 

```json
7.5
```

```json
8
```

```json
9.1
```

## <a name="concentration_unit"></a>8. Property `Library preparation > concentration_unit`

**Title:** Library concentration unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unit by which the library concentration was measured.

**Examples:** 

```json
"UO:0000275"
```

```json
"nanogram per mililiter"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="total_yield_value"></a>9. Property `Library preparation > total_yield_value`

**Title:** Library final yield value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Total yield of prepared library.

**Examples:** 

```json
7.5
```

```json
8
```

```json
9.1
```

## <a name="total_yield_unit"></a>10. Property `Library preparation > total_yield_unit`

**Title:** Library final yield unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unit by which the final yield of the library preparation was measured.

**Examples:** 

```json
"UO:0000024"
```

```json
"microliter"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="cdna_pcr_cycles"></a>11. Property `Library preparation > cdna_pcr_cycles`

**Title:** Number of iterations of cDNA amplification

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** The number of PCR cycles to amplify initial template material used as input for library preparation.

**Examples:** 

```json
10
```

```json
30
```

## <a name="pcr_cycles_for_indexing"></a>12. Property `Library preparation > pcr_cycles_for_indexing`

**Title:** Number of PCR cycles for indexing

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** The number of PCR cycles to incorporate a single or dual sample index and sequencing adapters.

**Examples:** 

```json
8
```

```json
10
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-29 at 09:57:57 +0000
