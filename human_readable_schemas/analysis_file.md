# Analysis file

- [1. Property `Analysis file > checksum`](#checksum)
- [2. Property `Analysis file > extension`](#extension)
- [3. Property `Analysis file > genome_assembly_version`](#genome_assembly_version)
- [4. Property `Analysis file > genome_patch_version`](#genome_patch_version)
- [5. Property `Analysis file > label`](#label)

**Title:** Analysis file

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A file analysis results produced by an analysis pipeline.

| Property                                               | Pattern | Type             | Deprecated | Definition                        | Title/Description |
| ------------------------------------------------------ | ------- | ---------------- | ---------- | --------------------------------- | ----------------- |
| - [checksum](#checksum )                               | No      | string           | No         | In #/definitions/non_empty_string | Checksum          |
| + [extension](#extension )                             | No      | string           | No         | Same as [checksum](#checksum )    | File extension    |
| - [genome_assembly_version](#genome_assembly_version ) | No      | enum (of string) | No         | Same as [checksum](#checksum )    | Genome version    |
| - [genome_patch_version](#genome_patch_version )       | No      | string           | No         | Same as [checksum](#checksum )    | Patch version     |
| + [label](#label )                                     | No      | string           | No         | In #/definitions/entity_id        | File name         |

## <a name="checksum"></a>1. Property `Analysis file > checksum`

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

## <a name="extension"></a>2. Property `Analysis file > extension`

**Title:** File extension

|                        |                       |
| ---------------------- | --------------------- |
| **Type**               | `string`              |
| **Required**           | Yes                   |
| **Same definition as** | [checksum](#checksum) |

**Description:** The extension of the file. Please indicate the full file extension including compression extensions.

**Examples:** 

```json
"h5"
```

```json
"mtx"
```

## <a name="genome_assembly_version"></a>3. Property `Analysis file > genome_assembly_version`

**Title:** Genome version

|                        |                       |
| ---------------------- | --------------------- |
| **Type**               | `enum (of string)`    |
| **Required**           | No                    |
| **Same definition as** | [checksum](#checksum) |

**Description:** Name of the genome assembly used to generate this file. Please use the name as defined in the Genome Reference Consortium (https://www.ncbi.nlm.nih.gov/grc).

**Examples:** 

```json
"GRCh37"
```

```json
"GRCh38"
```

```json
"Not applicable"
```

## <a name="genome_patch_version"></a>4. Property `Analysis file > genome_patch_version`

**Title:** Patch version

|                        |                       |
| ---------------------- | --------------------- |
| **Type**               | `string`              |
| **Required**           | No                    |
| **Same definition as** | [checksum](#checksum) |

**Description:** Patch version of the genome assembly used to generate this file.

**Examples:** 

```json
"p11"
```

```json
"p14"
```

## <a name="label"></a>5. Property `Analysis file > label`

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-11-08 at 15:14:05 +0000
