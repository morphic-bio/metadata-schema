# Differentiated cell line

- [1. Property `Differentiated cell line > label`](#label)
- [2. Property `Differentiated cell line > description`](#description)
- [3. Property `Differentiated cell line > culture_medium`](#culture_medium)
- [4. Property `Differentiated cell line > terminally_differentiated`](#terminally_differentiated)
- [5. Property `Differentiated cell line > model_system`](#model_system)
- [6. Property `Differentiated cell line > timepoint_value`](#timepoint_value)
- [7. Property `Differentiated cell line > timepoint_unit`](#timepoint_unit)

**Title:** Differentiated cell line

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the differentiated cell line.

| Property                                                   | Pattern | Type             | Deprecated | Definition | Title/Description                    |
| ---------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------ |
| + [label](#label )                                         | No      | string           | No         | -          | Differentiated cell line label       |
| - [description](#description )                             | No      | string           | No         | -          | Differentiated cell line description |
| - [culture_medium](#culture_medium )                       | No      | string           | No         | -          | Culture medium                       |
| + [terminally_differentiated](#terminally_differentiated ) | No      | enum (of string) | No         | -          | Terminally differentiated?           |
| - [model_system](#model_system )                           | No      | string           | No         | -          | Model system                         |
| + [timepoint_value](#timepoint_value )                     | No      | number           | No         | -          | Timepoint value                      |
| + [timepoint_unit](#timepoint_unit )                       | No      | string           | No         | -          | Timepoint unit                       |

## <a name="label"></a>1. Property `Differentiated cell line > label`

**Title:** Differentiated cell line label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the differentiated cell line.

**Example:** 

```json
"kolf2_2j_knockout_1_trophoblast"
```

| Restrictions                      |                                                                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                                                    |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22kolf2_2j_knockout_1_trophoblast%22) |

## <a name="description"></a>2. Property `Differentiated cell line > description`

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

## <a name="culture_medium"></a>3. Property `Differentiated cell line > culture_medium`

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

## <a name="terminally_differentiated"></a>4. Property `Differentiated cell line > terminally_differentiated`

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

## <a name="model_system"></a>5. Property `Differentiated cell line > model_system`

**Title:** Model system

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** To which model system this differentiated cell line has been derived into

**Examples:** 

```json
"UBERON:0000006"
```

```json
"islet of Langerhans"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="timepoint_value"></a>6. Property `Differentiated cell line > timepoint_value`

**Title:** Timepoint value

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |

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

## <a name="timepoint_unit"></a>7. Property `Differentiated cell line > timepoint_unit`

**Title:** Timepoint unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

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
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-05-21 at 13:25:13 +0000
