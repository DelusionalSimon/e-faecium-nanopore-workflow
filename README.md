# Unmasking a Superbug: *E. faecium* ST177 Workflow

This repository contains the complete computational workflow used to assemble and analyze the genome of a Vancomycin-Resistant *Enterococcus faecium* ST177 isolate, as detailed in the paper:

**Unmasking a Superbug: Nanopore Sequencing Reveals Chromosomal *vanB* and Resistance Plasmids in VRE *Enterococcus faecium* ST177**

This workflow is an archive intended to ensure full reproducibility of the paper's findings.


## Workflow Overview

This pipeline processes raw Oxford Nanopore `.fastq` reads to produce a fully assembled and annotated genome, complete with resistome and virulence factor identification.

The workflow is as follows:
1.  **QC:** Raw reads are filtered for quality using `fastplong`.
2.  **HPC Assembly:** Filtered reads are assembled on an HPC using `Flye` and `Kraken2` (for contamination checks).
3.  **QC Assessment:** The assembly is assessed using `QUAST`.
4.  **Annotation:** The final assembly is annotated with `Bakta` (for the full genome), `AMRFinderPlus` (for the resistome), `mlst` (for sequence typing), and `PlasmidFinder` (for replicons).
5. **Analysis:**


## How to Reproduce This Analysis

### Prerequisites
* [Conda](https://docs.conda.io/en/latest/miniconda.html)
* [Singularity](https://sylabs.io/docs/) (for the HPC steps)
* Access to a Slurm-based HPC (or modification of the `.slurm` scripts for your system)
* The raw sequencing data.

### Data Availability
The raw sequencing data for this project is not publicly archived yet. The raw .fastq file may be made available upon reasonable request to the corresponding author.

### Clone this repository:
    git https://github.com/DelusionalSimon/e-faecium-nanopore-workflow.git

    cd e-faecium-nanopore-workflow 

## Run the workflow in the Jupyter notebook

[Enter Complete_analysis.ipynb notebook](/notebooks/Complete_Analysis.ipynb)

## License
Distributed under the MIT License. See LICENSE.txt for more information.
