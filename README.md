# Unmasking a Superbug: *E. faecium* ST177 Workflow

This repository contains the complete computational workflow used to assemble and analyze the genome of a Vancomycin-Resistant *Enterococcus faecium* ST177 isolate, as detailed in the paper:

**Unmasking a Superbug: Nanopore Sequencing Reveals Chromosomal *vanB* and Resistance Plasmids in VRE *Enterococcus faecium* ST177**

This workflow is an archive intended to ensure full reproducibility of the paper's findings.


## Workflow Overview

This pipeline processes raw Oxford Nanopore `.fastq` reads to produce a fully assembled and annotated genome, complete with resistome and virulence factor identification.

The workflow is as follows:
1.  **Local Filtering and QC:** Raw reads are filtered for quality using `fastplong`.
2.  **HPC workflow:** `Kraken2` is used to verify the species of the isolate and check for contamination. Filtered reads are assembled on an HPC using `Flye`. This assembly is quality controlled using `QUAST`. 
4.  **Local Annotation and Typing:** The final assembly is annotated with `Bakta` (for the full genome) and `AMRFinderPlus` (for the resistome). `mlst` is utilized to find the sequence type.
5.  **Web Based Analysis:** The `PlasmidFinder` web tool is used to identify replicons on the plasmids. `Gemini` is used to identify interesting operons and gene clusters using the annotated data.   


## How to Reproduce This Analysis

### Prerequisites
* [Conda](https://docs.conda.io/en/latest/miniconda.html)
* [Singularity](https://sylabs.io/docs/) (for the HPC steps)
* Access to a Slurm-based HPC (or a modification of `HPC_orchestrator.py` and the `.slurm` scripts to run them locally on your system)
* Raw sequencing data.

### HPC Container Setup
The HPC workflow runs all tools (Kraken2, Flye, QUAST) inside Singularity containers. Such containers can be accessed from the BioContainers project.

Before running the HPC scripts, you must pull the necessary containers to your cluster, this can be done with the `singularity pull` command. Then you need to specify their paths in `HPC_config.py`. 

### Data Availability
The raw sequencing data for this project is not publicly archived. The raw .fastq file may be made available upon reasonable request.

### Clone this repository:
Run 
```git clone https://github.com/DelusionalSimon/e-faecium-nanopore-workflow.git``` where you want to download the project


followed by ```cd e-faecium-nanopore-workflow``` to enter the folder.  

## Run the workflow in the Jupyter notebook

[Enter Complete_analysis.ipynb notebook](/notebooks/Complete_Analysis.ipynb)


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


