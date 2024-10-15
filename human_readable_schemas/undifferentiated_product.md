# Undifferentiated product

- [1. Property `Undifferentiated product > label`](#label)
- [2. Property `Undifferentiated product > description`](#description)
- [3. Property `Undifferentiated product > undifferentiated_product_protocol_id`](#undifferentiated_product_protocol_id)
- [4. Property `Undifferentiated product > timepoint_value`](#timepoint_value)
- [5. Property `Undifferentiated product > timepoint_unit`](#timepoint_unit)
- [6. Property `Undifferentiated product > treatment_condition`](#treatment_condition)
- [7. Property `Undifferentiated product > wt_control_status`](#wt_control_status)

**Title:** Undifferentiated product

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the undifferentiated product.

| Property                                                                         | Pattern | Type             | Deprecated | Definition | Title/Description                    |
| -------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------ |
| + [label](#label )                                                               | No      | string           | No         | -          | Undifferentiated product ID          |
| - [description](#description )                                                   | No      | string           | No         | -          | Undifferentiated product description |
| + [undifferentiated_product_protocol_id](#undifferentiated_product_protocol_id ) | No      | string           | No         | -          | Undifferentiated product protocol ID |
| - [timepoint_value](#timepoint_value )                                           | No      | integer          | No         | -          | Timepoint value                      |
| - [timepoint_unit](#timepoint_unit )                                             | No      | string           | No         | -          | Timepoint unit                       |
| - [treatment_condition](#treatment_condition )                                   | No      | string           | No         | -          | Treatment/Condition                  |
| - [wt_control_status](#wt_control_status )                                       | No      | enum (of string) | No         | -          | WT/Control status                    |

## <a name="label"></a>1. Property `Undifferentiated product > label`

**Title:** Undifferentiated product ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the undifferentiated product. To be filled in only when differentiation has not been carried out and for undifferentiated products went into assaying.. No spaces allowed.

**Examples:** 

```json
"Ocm108_Parent_Auxin_100um_24h_rep2"
```

```json
"kf201_GP_untreated"
```

| Restrictions                      |                                                                                                                                         |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                                       |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22Ocm108_Parent_Auxin_100um_24h_rep2%22) |

## <a name="description"></a>2. Property `Undifferentiated product > description`

**Title:** Undifferentiated product description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the undifferentiated product.

**Examples:** 

```json
"KOLF2.2 \"Parent\" with OSTIR receptor expression treated with DMSO"
```

```json
"Unmodified \"Grandparent\" KOLF2.2 treated with DMSO"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="undifferentiated_product_protocol_id"></a>3. Property `Undifferentiated product > undifferentiated_product_protocol_id`

**Title:** Undifferentiated product protocol ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** An ID for the protocol applied on the undifferentiated product (if applicable). No spaces allowed.

**Examples:** 

```json
"Auxin_induction_cell_line"
```

```json
"DMSO_treated_iPSC"
```

| Restrictions                      |                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                                              |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22Auxin_induction_cell_line%22) |

## <a name="timepoint_value"></a>4. Property `Undifferentiated product > timepoint_value`

**Title:** Timepoint value

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Value of the timepoint. Only integers accepted.

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

## <a name="timepoint_unit"></a>5. Property `Undifferentiated product > timepoint_unit`

**Title:** Timepoint unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

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

## <a name="treatment_condition"></a>6. Property `Undifferentiated product > treatment_condition`

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

## <a name="wt_control_status"></a>7. Property `Undifferentiated product > wt_control_status`

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
