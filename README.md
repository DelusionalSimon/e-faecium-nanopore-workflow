# Unmasking a Superbug: *E. faecium* ST177 Workflow

This repository contains the complete, end-to-end computational workflow used to assemble and analyze the genome of a Vancomycin-Resistant *Enterococcus faecium* ST177 isolate.

It serves as a **reproducible case study** for a full genomic analysis, from raw Oxford Nanopore reads to a final annotated assembly, including resistome and virulence factor identification.

It can be used to run similar analyses using your own or publicly available long read data in a `.fastq` format. 


## Workflow Overview

This pipeline processes raw Oxford Nanopore `.fastq` reads to produce a fully assembled and annotated genome, complete with resistome and virulence factor identification.

The workflow is as follows:
1.  **Local Filtering and QC:** Raw reads are filtered for quality using `fastplong`.
2.  **HPC workflow:** `Kraken2` is used to verify the species of the isolate and check for contamination. Filtered reads are assembled on an HPC using `Flye`. This assembly is quality controlled using `QUAST`. 
3.  **Local Annotation and Typing:** The final assembly is annotated with `Bakta` (for the full genome) and `AMRFinderPlus` (for the resistome). `mlst` is utilized to find the sequence type.
4.  **Web Based Analysis:** The `PlasmidFinder` web tool is used to identify replicons on the plasmids. `Gemini` is used to identify interesting operons and gene clusters using the annotated data.   


### Prerequisites
* [Conda](https://docs.conda.io/en/latest/miniconda.html)
* [Singularity](https://sylabs.io/docs/) (for the HPC steps)
* Access to a Slurm-based HPC (or a modification of `HPC_orchestrator.py` and the `.slurm` scripts to run them locally on your system)
* A unix based system like WSL

### HPC Container Setup
The HPC workflow runs all tools (Kraken2, Flye, QUAST) inside Singularity containers. Such containers can be accessed from the BioContainers project.

Before running the HPC scripts, you must pull the necessary containers to your cluster, this can be done with the `singularity pull` command. Then you need to specify their paths in `HPC_config.py`. 

### Clone this repository:
Run 
```git clone https://github.com/DelusionalSimon/e-faecium-nanopore-workflow.git``` in your command line where you want to download the project


followed by ```cd e-faecium-nanopore-workflow``` to enter the folder.  

### Set up the environment
Create the conda environment by running `conda env create -f environment.yml` in the terminal

Activate the environment by running `conda activate efaecium_env`

Use this environment as the kernel for the jupyter notebook below.

## Run the workflow in the Jupyter notebook
Move on to the Jupyter Notebook detailing the whole workflow:

[Complete Analysis Notebook](/notebooks/Complete_Analysis.ipynb)


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


