"""
This config file contains configuration settings for the HPC environment.
It is used to set up paths and parameters specific to the HPC cluster. 
Please ensure to modify the settings according to your HPC cluster requirements.

For local configurations, please refer to the config.yaml file located at the 
root of the repository.   
"""
import os

# Containers
KRAKEN_CONTAINER_PATH = "/cephyr/users/hasimon/Vera/home/user/containers/kraken2.sif"

# Databases
KRAKEN_DB_PATH = "/cephyr/NOBACKUP/groups/n2bin_gu/BIO511/ref_dbs/kraken2db"

# HPC Base Directory
HPC_STORAGE_DIR = "/cephyr/NOBACKUP/groups/n2bin_gu/students/hasimon/e-faecium"

# Input and Output Paths
FILTERED_FASTQ_FILE = "CCUG-33829.filtered.fastq.gz"
FASTQ_PATH= os.path.join(HPC_STORAGE_DIR, "data", FILTERED_FASTQ_FILE)
LOGS_PATH = os.path.join(HPC_STORAGE_DIR, "logs")
RESULTS_PATH = os.path.join(HPC_STORAGE_DIR, "results")
