# Adaptations HCA --> Morphic

## Technical changes
- "describedBy" fields to point out to github raw instead of the bucket deployment of HCA schemas

## Schema changelog

E = Entity

F = Field

### Project

**Added**
- `project.target_genes` (F)

**Deleted**
- `project.estimated_cell_count` (F)
- `project.publications.official_hca_publication` (F)


### Cell line
**Added**
- `cell_line.genbank_assembly_accession` (F)

### Protocols
**Added**
- `type/protocol/biomaterial_collection/gene_silencing_protocol.json` (E)
- `module/protocol/crisproff.json` (E)

### Ontology

**Added**
- `module/ontology/target_gene_ontology.json` (E)
- `module/ontology/gene_silencing_method_ontology.json` (E)

# Potential improvements list
- Adapt to Json Schema draft 09
- Add cellosaurus ontology
- Gene silencing method needs to point to correct ontology
- Rather than a gene silencing protocol, it may be better to add a gene expression alteration protocol (More broad, could be used for both increase and decrease of expression (e.g. could be used for CRISPRon))