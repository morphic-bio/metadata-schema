# Differentiated product

- [1. Property `Differentiated product > label`](#label)
- [2. Property `Differentiated product > description`](#description)
- [3. Property `Differentiated product > differentiated_product_protocol_id`](#differentiated_product_protocol_id)
- [4. Property `Differentiated product > terminally_differentiated`](#terminally_differentiated)
- [5. Property `Differentiated product > model_system`](#model_system)
- [6. Property `Differentiated product > timepoint_value`](#timepoint_value)
- [7. Property `Differentiated product > timepoint_unit`](#timepoint_unit)
- [8. Property `Differentiated product > treatment_condition`](#treatment_condition)
- [9. Property `Differentiated product > wt_control_status`](#wt_control_status)

**Title:** Differentiated product

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the differentiated product.

| Property                                                                     | Pattern | Type             | Deprecated | Definition | Title/Description                  |
| ---------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------------------- |
| + [label](#label )                                                           | No      | string           | No         | -          | Differentiated product ID          |
| - [description](#description )                                               | No      | string           | No         | -          | Differentiated product description |
| + [differentiated_product_protocol_id](#differentiated_product_protocol_id ) | No      | string           | No         | -          | Differentiated product protocol ID |
| + [terminally_differentiated](#terminally_differentiated )                   | No      | enum (of string) | No         | -          | Terminally differentiated?         |
| - [model_system](#model_system )                                             | No      | string           | No         | -          | Model system                       |
| + [timepoint_value](#timepoint_value )                                       | No      | integer          | No         | -          | Timepoint value                    |
| + [timepoint_unit](#timepoint_unit )                                         | No      | string           | No         | -          | Timepoint unit                     |
| - [treatment_condition](#treatment_condition )                               | No      | string           | No         | -          | Treatment/Condition                |
| - [wt_control_status](#wt_control_status )                                   | No      | enum (of string) | No         | -          | WT/Control status                  |

## <a name="label"></a>1. Property `Differentiated product > label`

**Title:** Differentiated product ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the differentiated product. No spaces allowed.

**Example:** 

```json
"kolf2_2j_knockout_1_trophoblast"
```

| Restrictions                      |                                                                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                                                    |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22kolf2_2j_knockout_1_trophoblast%22) |

## <a name="description"></a>2. Property `Differentiated product > description`

**Title:** Differentiated product description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the differentiated product.

**Example:** 

```json
"KOLF2.2J derived knockout cell line, PAX6/STL2 DKO, differentiated into trophoblasts"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="differentiated_product_protocol_id"></a>3. Property `Differentiated product > differentiated_product_protocol_id`

**Title:** Differentiated product protocol ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** An ID for the differentiation protocol used. No spaces allowed.

**Examples:** 

```json
"JAXPD002"
```

```json
"EB_Protocol_Final_Merged.pdf"
```

```json
"msk_pancreatic_diff_protocol"
```

| Restrictions                      |                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                             |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22JAXPD002%22) |

## <a name="terminally_differentiated"></a>4. Property `Differentiated product > terminally_differentiated`

**Title:** Terminally differentiated?

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Is the cell line terminally differentiated.

**Examples:** 

```json
"no"
```

```json
"unknown"
```

```json
"yes"
```

Must be one of:
* "yes"
* "no"
* "unknown"

## <a name="model_system"></a>5. Property `Differentiated product > model_system`

**Title:** Model system

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** To which model system this differentiated cell line has been derived into

**Examples:** 

```json
"cardioid"
```

```json
"pancreatic gut"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="timepoint_value"></a>6. Property `Differentiated product > timepoint_value`

**Title:** Timepoint value

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Value of the timepoint. Please include the value only as a number.

**Examples:** 

```json
7
```

```json
8
```

```json
9
```

## <a name="timepoint_unit"></a>7. Property `Differentiated product > timepoint_unit`

**Title:** Timepoint unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Unit of the timepoint.

**Examples:** 

```json
"UO:0000010"
```

```json
"second"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="treatment_condition"></a>8. Property `Differentiated product > treatment_condition`

**Title:** Treatment/Condition

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Protocol for generating cell line. e.g. condition or multiple conditions used to generate the cell line. (if applicable)

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

## <a name="wt_control_status"></a>9. Property `Differentiated product > wt_control_status`

**Title:** WT/Control status

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Indicate the controls used the experiment. (if applicable)

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
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-15 at 13:00:36 +0000
