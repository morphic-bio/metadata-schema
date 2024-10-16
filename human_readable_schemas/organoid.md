# Organoid

- [1. Property `Organoid > label`](#label)
- [2. Property `Organoid > description`](#description)
- [3. Property `Organoid > model_system`](#model_system)
- [4. Property `Organoid > age_unit`](#age_unit)
- [5. Property `Organoid > age_value`](#age_value)
- [6. Property `Organoid > embedded_in_matrigel`](#embedded_in_matrigel)
- [7. Property `Organoid > growth_environment`](#growth_environment)
- [8. Property `Organoid > morphology`](#morphology)
- [9. Property `Organoid > size_value`](#size_value)
- [10. Property `Organoid > size_unit`](#size_unit)
- [11. Property `Organoid > stored_oxygen_levels`](#stored_oxygen_levels)

**Title:** Organoid

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Information about the organoid.

| Property                                         | Pattern | Type    | Deprecated | Definition | Title/Description     |
| ------------------------------------------------ | ------- | ------- | ---------- | ---------- | --------------------- |
| + [label](#label )                               | No      | string  | No         | -          | Organoid label        |
| - [description](#description )                   | No      | string  | No         | -          | Organoid description  |
| + [model_system](#model_system )                 | No      | string  | No         | -          | Model system          |
| - [age_unit](#age_unit )                         | No      | string  | No         | -          | Age unit              |
| - [age_value](#age_value )                       | No      | number  | No         | -          | Organoid age          |
| - [embedded_in_matrigel](#embedded_in_matrigel ) | No      | boolean | No         | -          | Embeddded in matrigel |
| - [growth_environment](#growth_environment )     | No      | string  | No         | -          | Growth environment    |
| - [morphology](#morphology )                     | No      | string  | No         | -          | Organoid morphology   |
| - [size_value](#size_value )                     | No      | number  | No         | -          | Organoid size         |
| - [size_unit](#size_unit )                       | No      | string  | No         | -          | Size unit             |
| - [stored_oxygen_levels](#stored_oxygen_levels ) | No      | number  | No         | -          | Stored oxygen level   |

## <a name="label"></a>1. Property `Organoid > label`

**Title:** Organoid label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `regex`  |

**Description:** A unique label for the organoid. No spaces allowed.

**Example:** 

```json
"kolf2_2j_knockout_1"
```

| Restrictions                      |                                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Min length**                    | 1                                                                                                                        |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22kolf2_2j_knockout_1%22) |

## <a name="description"></a>2. Property `Organoid > description`

**Title:** Organoid description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A general description of the organoid.

**Example:** 

```json
"Neuroectoderm organoid, derived from kolf2_2j DKO"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="model_system"></a>3. Property `Organoid > model_system`

**Title:** Model system

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

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

## <a name="age_unit"></a>4. Property `Organoid > age_unit`

**Title:** Age unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unit by which the age of the organoid was measured

**Examples:** 

```json
"UO:0000033"
```

```json
"week"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="age_value"></a>5. Property `Organoid > age_value`

**Title:** Organoid age

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Age of the organoid in Organoid age unit measured from when cell aggregates started differentiating to desired organoid model.

**Examples:** 

```json
55
```

```json
67
```

## <a name="embedded_in_matrigel"></a>6. Property `Organoid > embedded_in_matrigel`

**Title:** Embeddded in matrigel

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Whether the organoid is embedded in a matrigel.

**Examples:** 

```json
false
```

```json
true
```

## <a name="growth_environment"></a>7. Property `Organoid > growth_environment`

**Title:** Growth environment

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Growth environment in which the organoid is grown.

**Examples:** 

```json
"adherent"
```

```json
"liquid suspension"
```

```json
"matrigel"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="morphology"></a>8. Property `Organoid > morphology`

**Title:** Organoid morphology

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** General description of the organoid morphology.

**Examples:** 

```json
"Epithelial monolayer with budding crypt-like domains"
```

```json
"Optic cup structure"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="size_value"></a>9. Property `Organoid > size_value`

**Title:** Organoid size

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Size of the organoid in Organoid size unit.

**Examples:** 

```json
4
```

```json
5
```

## <a name="size_unit"></a>10. Property `Organoid > size_unit`

**Title:** Size unit

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unit by which the size of the organoid was measured.

**Examples:** 

```json
"UO:0000015"
```

```json
"millimeter"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="stored_oxygen_levels"></a>11. Property `Organoid > stored_oxygen_levels`

**Title:** Stored oxygen level

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Percent oxygen level organoid was stored in prior to sequencing.

**Examples:** 

```json
75
```

```json
80
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-15 at 13:00:36 +0000
