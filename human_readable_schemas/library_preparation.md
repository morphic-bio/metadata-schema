# Library preparation

- [1. Property `Library preparation > average_fragment_size`](#average_fragment_size)
- [2. Property `Library preparation > description`](#description)
- [3. Property `Library preparation > label`](#label)
- [4. Property `Library preparation > library_concentration_unit`](#library_concentration_unit)
- [5. Property `Library preparation > library_concentration_value`](#library_concentration_value)
- [6. Property `Library preparation > library_final_yield_unit`](#library_final_yield_unit)
- [7. Property `Library preparation > library_final_yield_value`](#library_final_yield_value)
- [8. Property `Library preparation > library_input_amount_unit`](#library_input_amount_unit)
- [9. Property `Library preparation > library_input_amount_value`](#library_input_amount_value)
- [10. Property `Library preparation > library_pcr_cycles`](#library_pcr_cycles)

**Title:** Library preparation

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the library preparation.

| Property                                                       | Pattern | Type    | Deprecated | Definition | Title/Description               |
| -------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------- |
| - [average_fragment_size](#average_fragment_size )             | No      | integer | No         | -          | Average fragment size           |
| - [description](#description )                                 | No      | string  | No         | -          | Library preparation description |
| + [label](#label )                                             | No      | string  | No         | -          | Library preparation label       |
| - [library_concentration_unit](#library_concentration_unit )   | No      | string  | No         | -          | Library concentration unit      |
| - [library_concentration_value](#library_concentration_value ) | No      | number  | No         | -          | Library concentration value     |
| - [library_final_yield_unit](#library_final_yield_unit )       | No      | string  | No         | -          | Library final yield unit        |
| - [library_final_yield_value](#library_final_yield_value )     | No      | number  | No         | -          | Library final yield value       |
| - [library_input_amount_unit](#library_input_amount_unit )     | No      | string  | No         | -          | Library input amount unit       |
| - [library_input_amount_value](#library_input_amount_value )   | No      | number  | No         | -          | Library input amount value      |
| - [library_pcr_cycles](#library_pcr_cycles )                   | No      | integer | No         | -          | Library PCR cycles              |

## <a name="average_fragment_size"></a>1. Property `Library preparation > average_fragment_size`

**Title:** Average fragment size

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Average fragment size for the transcripts in the library preparation.

**Examples:** 

```json
150
```

```json
256
```

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

## <a name="label"></a>3. Property `Library preparation > label`

**Title:** Library preparation label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the library preparation.

**Example:** 

```json
"kolf2_2j_knockout_1_trophoblast_library_preparation1S"
```

| Restrictions                      |                                                                                                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                                          |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22kolf2_2j_knockout_1_trophoblast_library_preparation1S%22) |

## <a name="library_concentration_unit"></a>4. Property `Library preparation > library_concentration_unit`

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

## <a name="library_concentration_value"></a>5. Property `Library preparation > library_concentration_value`

**Title:** Library concentration value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Value of the library concentration.

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

## <a name="library_final_yield_unit"></a>6. Property `Library preparation > library_final_yield_unit`

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

## <a name="library_final_yield_value"></a>7. Property `Library preparation > library_final_yield_value`

**Title:** Library final yield value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Value of the library final yield.

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

## <a name="library_input_amount_unit"></a>8. Property `Library preparation > library_input_amount_unit`

**Title:** Library input amount unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unit by which the value of the library input was measured.

**Examples:** 

```json
"UO:0000010"
```

```json
"UO:0000034"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="library_input_amount_value"></a>9. Property `Library preparation > library_input_amount_value`

**Title:** Library input amount value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Value of the library input amount.

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

## <a name="library_pcr_cycles"></a>10. Property `Library preparation > library_pcr_cycles`

**Title:** Library PCR cycles

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Number of PCR cycles performed for this library.

**Examples:** 

```json
150
```

```json
256
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-11-09 at 14:31:24 +0000
