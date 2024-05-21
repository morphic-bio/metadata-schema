# MorPhiC Metadata Schema

This repository contains a modified version of the Human Cell Atlas Metadata Schema, obtained from their repository.

This is a tentative first approach at metadata standardisation and validation for the MorPhiC consortia.

As such, it will be constantly evolving and adapting to the community needs.

**To suggest updates**, please use the best option for yourself:
- Single/Small request: [open an issue](https://github.com/morphic-bio/metadata-schema/issues/new) using the template for schema updates provided by the repository
- Bulk request/Whole schema: Please download [this spreadsheet](https://docs.google.com/spreadsheets/d/1GhoIGanB5VgO3RotiJWev-q5E097IefpMaP7e2Ktyck/edit#gid=0) locally, fill it out,
and send it to the [MorPhiC Helpdesk via e-mail](mailto:helpdesk@morphic.bio)

# Metadata model

For the metadata model, we suggest a similar approach to the Human Cell Atlas; i.e.defining each step of the experimental process as a separate entity and linking all the entities together to form an experimental graph. With this model, any step in the experiment (e.g. sequence file `​​GT22_04578_R1.fastq.gz`) can lead the user through the experiment, extracting the important metadata in the process of reconstructing the assay.

The suggested metadata model is comprised of 3 main types of information:

**General information about the project**
- Attributes: a unique identifier, a description, institutions involved, etc.
- Use: To be displayed on a catalogue or the data portal when available

**Information of scientific value for each of the samples (sample metadata)**
- Attributes: age of the donor, type of gene expression alteration, etc.
- Use: To be displayed as filters on the data portal when available, collected in a standardised way so that analysis/data collection tools can be developed over the MorPhiC collection of data.

**Information about the data files (file metadata)**
- Attributes: file name, content of the file, description, read index (In the case of RNA-Seq experiments), etc
- Use: allows analysis, quality control filters and helps develop standardised analysis workflows with little to none manual input.

Alongside the metadata model, we are also trying to understand and organise the data model, by organising each of the entities described into a graph that can be parsed, understood and visualised.


## Transcriptomics

![Consolidated Workflow](Assets/Morphic%20consolidated.jpg)

