# Undifferentiated product

- [1. Property `Undifferentiated product > label`](#label)
- [2. Property `Undifferentiated product > description`](#description)
- [3. Property `Undifferentiated product > timepoint_value`](#timepoint_value)
- [4. Property `Undifferentiated product > timepoint_unit`](#timepoint_unit)

**Title:** Undifferentiated product

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the undifferentiated product.

| Property                               | Pattern | Type   | Deprecated | Definition | Title/Description                    |
| -------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------ |
| + [label](#label )                     | No      | string | No         | -          | Undifferentiated product ID          |
| - [description](#description )         | No      | string | No         | -          | Differentiated cell line description |
| - [timepoint_value](#timepoint_value ) | No      | number | No         | -          | Timepoint value                      |
| - [timepoint_unit](#timepoint_unit )   | No      | string | No         | -          | Timepoint unit                       |

## <a name="label"></a>1. Property `Undifferentiated product > label`

**Title:** Undifferentiated product ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique ID for the undifferentiated product.

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

**Title:** Differentiated cell line description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the differentiated cell line.

**Example:** 

```json
"KOLF2.2J derived knockout cell line, PAX6/STL2 DKO, differentiated into trophoblasts"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="timepoint_value"></a>3. Property `Undifferentiated product > timepoint_value`

**Title:** Timepoint value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Value of the timepoint.

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

## <a name="timepoint_unit"></a>4. Property `Undifferentiated product > timepoint_unit`

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-08-19 at 09:45:08 +0000
