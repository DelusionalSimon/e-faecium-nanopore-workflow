"""
This config file contains configuration settings for the HPC environment.
It is used to set up paths and parameters specific to the HPC cluster. 
Please ensure to modify the settings according to your HPC cluster requirements.

For local configurations, please refer to the config.yaml file located at the 
root of the repository.   
"""
import os


# ----------[CORE]----------
# HPC Base Directory
HPC_STORAGE_DIR = "/cephyr/NOBACKUP/groups/n2bin_gu/students/hasimon/e-faecium"

# Input and Output Paths
DATA_PATH = os.path.join(HPC_STORAGE_DIR, "data")
FILTERED_FASTQ_FILE = "CCUG-33829.filtered.fastq.gz"
FASTQ_PATH= os.path.join(DATA_PATH, FILTERED_FASTQ_FILE)
LOGS_PATH = os.path.join(HPC_STORAGE_DIR, "logs")
RESULTS_PATH = os.path.join(HPC_STORAGE_DIR, "results")

# HPC Settings 
ALLOCATION = "C3SE408-25-2"
PARTITION = "vera"


# ----------[KRAKEN2 PARAMETERS]----------
# Container
KRAKEN_CONTAINER_PATH = "/cephyr/users/hasimon/Vera/home/user/containers/kraken2.sif"

# Database  
KRAKEN_DB_PATH = "/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/ref_dbs/kraken2db"

# Job Specs
KRAKEN_CPUS = 12
KRAKEN_TIME = "01:00:00"
KRAKEN_JOB_NAME = "kraken2_classification"
KRAKEN_OUTPUT_LOG = os.path.join(LOGS_PATH, "kraken2_%j.out")
KRAKEN_ERROR_LOG = os.path.join(LOGS_PATH, "kraken2_%j.err")
KRAKEN_SLURM_SCRIPT = "01_kraken2.slurm"
KRAKEN_SLURM_PATH = os.path.join(HPC_STORAGE_DIR, KRAKEN_SLURM_SCRIPT)

# Outputs
KRAKEN_OUTPUT = "kraken2_output.txt"
KRAKEN_REPORT = "kraken2_report.txt"
KRAKEN_CLASSIFIED_FASTQ = "classified.fastq"
KRAKEN_UNCLASSIFIED_FASTQ = "unclassified.fastq"

# ----------[FLYE PARAMETERS]----------
# Container
FLYE_CONTAINER_PATH = "/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/singularity_images/flye.sif"

# Job Specs
FLYE_CPUS = 12
FLYE_TIME = "02:30:00"
FLYE_JOB_NAME = "flye_polished"
FLYE_OUTPUT_LOG = os.path.join(LOGS_PATH, "flye2_%j.out")
FLYE_ERROR_LOG = os.path.join(LOGS_PATH, "flye2_%j.err")
FLYE_SLURM_SCRIPT = "02_flye.slurm"
FLYE_SLURM_PATH = os.path.join(HPC_STORAGE_DIR, FLYE_SLURM_SCRIPT)

# Settings
FLYE_ITERATIONS = 5

# ----------[QUAST PARAMETERS]----------
# Container
QUAST_CONTAINER_PATH = "/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/singularity_images/quast.sif"

# Job Specs
QUAST_CPUS = 4
QUAST_TIME = "01:00:00"
QUAST_JOB_NAME = "quast_analysis"
QUAST_OUTPUT_LOG = os.path.join(LOGS_PATH, "quast2_%j.out")
QUAST_ERROR_LOG = os.path.join(LOGS_PATH, "quast2_%j.err")
QUAST_SLURM_SCRIPT = "03_quast.slurm"
QUAST_SLURM_PATH = os.path.join(HPC_STORAGE_DIR, QUAST_SLURM_SCRIPT)

# Input
QUAST_ASSEMBLY_DIR = os.path.join(RESULTS_PATH, "flye")