"""!
@file       00_HPC_orchestrator.py
@author     Simon Håkansson
@date       2025-10-24
@brief      This script orchestrates the submission of HPC jobs.

@details    This script reads the HPC configuration from HPC_config.py
            and submits jobs to the HPC scheduler based on the defined 
            parameters. It is designed to streamline the process of running
            bioinformatics analyses on an HPC cluster.
"""
# ----------[IMPORTS]----------
import os
import subprocess
import HPC_config
import argparse

# ----------[CONFIGURATION]----------
# Load HPC configuration
logs_path =  HPC_config.LOGS_PATH
results_path = HPC_config.RESULTS_PATH
fastq_data = HPC_config.FASTQ_PATH

# Kraken2 parameters
kraken_output_log = os.path.join(logs_path, "kraken2_%j.out")
kraken_error_log = os.path.join(logs_path, "kraken2_%j.err")
kraken_container_path = HPC_config.KRAKEN_CONTAINER_PATH
kraken_db_path = HPC_config.KRAKEN_DB_PATH



# ----------[FUNCTIONS]----------
def submit_kraken2_job():
    """!
    @brief:     Submits a Kraken2 job to the HPC scheduler.
    
    @details:   Constructs the sbatch command with appropriate parameters
                and submits the job using subprocess.
    """
    pass



# ----------[MAIN SCRIPT]----------
def main():
    """!
    @brief: Main function to orchestrate HPC job submissions.
    
    @details: Calls functions to submit various HPC jobs as needed. uses argparse
              to handle command-line arguments for flexibility.
    
    """
    


if __name__ == "__main__":
    main()