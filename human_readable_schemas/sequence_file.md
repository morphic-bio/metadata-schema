# Sequence file

- [1. Property `Sequence file > checksum`](#checksum)
- [2. Property `Sequence file > extension`](#extension)
- [3. Property `Sequence file > label`](#label)
- [4. Property `Sequence file > lane_index`](#lane_index)
- [5. Property `Sequence file > read_index`](#read_index)
- [6. Property `Sequence file > read_length`](#read_length)

**Title:** Sequence file

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A file of read sequences generated by a sequencing experiment.

| Property                       | Pattern | Type             | Deprecated | Definition                        | Title/Description |
| ------------------------------ | ------- | ---------------- | ---------- | --------------------------------- | ----------------- |
| - [checksum](#checksum )       | No      | string           | No         | In #/definitions/non_empty_string | Checksum          |
| + [extension](#extension )     | No      | string           | No         | Same as [checksum](#checksum )    | File extension    |
| + [label](#label )             | No      | string           | No         | In #/definitions/entity_id        | File name         |
| - [lane_index](#lane_index )   | No      | integer          | No         | -                                 | Lane index        |
| + [read_index](#read_index )   | No      | enum (of string) | No         | Same as [checksum](#checksum )    | Read index        |
| - [read_length](#read_length ) | No      | integer          | No         | -                                 | Read length       |

## <a name="checksum"></a>1. Property `Sequence file > checksum`

**Title:** Checksum

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `string`                       |
| **Required**   | No                             |
| **Defined in** | #/definitions/non_empty_string |

**Description:** MD5 checksum of the file.

**Example:** 

```json
"e09a986c2e630130b1849d4bf9a94c06"
```

**Example:** 

```json
"e09a986c2e630130b1849d4bf9a94c06"
```

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="extension"></a>2. Property `Sequence file > extension`

**Title:** File extension

|                        |                       |
| ---------------------- | --------------------- |
| **Type**               | `string`              |
| **Required**           | Yes                   |
| **Same definition as** | [checksum](#checksum) |

**Description:** The extension of the file. Please indicate the full file extension including compression extensions.

**Examples:** 

```json
"fastq.gz"
```

```json
"tif"
```

## <a name="label"></a>3. Property `Sequence file > label`

**Title:** File name

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | Yes                     |
| **Defined in** | #/definitions/entity_id |

**Description:** The name of the file. Please include the file extension in the file name.

**Examples:** 

```json
"R1.fastq.gz"
```

```json
"R2.fastq.gz"
```

**Examples:** 

```json
"R1.fastq.gz"
```

```json
"R2.fastq.gz"
```

| Restrictions                      |                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Min length**                    | 1                                                                                                                |
| **Must match regular expression** | ```^[a-zA-Z0-9_]*$``` [Test](https://regex101.com/?regex=%5E%5Ba-zA-Z0-9_%5D%2A%24&testString=%22R1.fastq.gz%22) |

## <a name="lane_index"></a>4. Property `Sequence file > lane_index`

**Title:** Lane index

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** The lane that this file was sequenced from.

**Examples:** 

```json
1
```

```json
4
```

## <a name="read_index"></a>5. Property `Sequence file > read_index`

**Title:** Read index

|                        |                       |
| ---------------------- | --------------------- |
| **Type**               | `enum (of string)`    |
| **Required**           | Yes                   |
| **Same definition as** | [checksum](#checksum) |

**Description:** The sequencing read this file represents. If a sequencing experiment is single-end, enter 'read1'.

**Examples:** 

```json
"index2"
```

```json
"read1"
```

## <a name="read_length"></a>6. Property `Sequence file > read_length`

**Title:** Read length

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** The length of a sequenced read in this file, in nucleotides.

**Examples:** 

```json
51
```

```json
150
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-11-08 at 15:14:05 +0000