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
import HPC_config as conf
import argparse


# ----------[FUNCTIONS]----------
def submit_kraken2_job():
    """!
    @brief:     Submits a Kraken2 job to the HPC scheduler.
    
    @details:   Constructs the sbatch command with appropriate parameters
                and submits the job using subprocess.
    """
    kraken_command = [
        "sbatch",
        # Slurm job specifications
        "-A", conf.ALLOCATION,
        "-p", conf.PARTITION,
        "-N", "1",
        "--cpus-per-task", str(conf.KRAKEN_CPUS),
        "-t", conf.KRAKEN_TIME,
        "-J", conf.KRAKEN_JOB_NAME,
        "--output", conf.KRAKEN_OUTPUT_LOG,
        "--error", conf.KRAKEN_ERROR_LOG,
        # The script to run
        conf.KRAKEN_SLURM_PATH,
        # Arguments to the slurm script
        conf.KRAKEN_CONTAINER_PATH,
        conf.KRAKEN_DB_PATH,
        conf.DATA_PATH,
        conf.RESULTS_PATH,
        conf.FILTERED_FASTQ_FILE,
        conf.KRAKEN_OUTPUT,
        conf.KRAKEN_REPORT,
        conf.KRAKEN_CLASSIFIED_FASTQ,
        conf.KRAKEN_UNCLASSIFIED_FASTQ
    ]
    
    # Submit the job
    try:
        subprocess.run(kraken_command, check=True)
        print("Kraken2 job submitted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error submitting Kraken2 job: {e}")

def submit_flye_job():
    """!
    @brief:     Submits a Flye assembly job to the HPC scheduler.
    
    @details:   Constructs the sbatch command with appropriate parameters
                and submits the job using subprocess.
    """
    flye_command = [
        "sbatch",
        # Slurm job specifications
        "-A", conf.ALLOCATION,
        "-p", conf.PARTITION,
        "-N", "1",
        "--cpus-per-task", str(conf.FLYE_CPUS),
        "-t", conf.FLYE_TIME,
        "-J", conf.FLYE_JOB_NAME,
        "--output", conf.FLYE_OUTPUT_LOG,
        "--error", conf.FLYE_ERROR_LOG,
        # The script to run
        conf.FLYE_SLURM_PATH,
        # Arguments to the slurm script
        conf.FLYE_CONTAINER_PATH,
        conf.DATA_PATH,
        conf.RESULTS_PATH,
        conf.FILTERED_FASTQ_FILE,
        str(conf.FLYE_ITERATIONS)
    ]
    
    # Submit the job
    try:
        subprocess.run(flye_command, check=True)
        print("Flye job submitted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error submitting Flye job: {e}")

def submit_quast_job():
    """!
    @brief:     Submits a QUAST analysis job to the HPC scheduler.
    
    @details:   Constructs the sbatch command with appropriate parameters
                and submits the job using subprocess.
    """
    quast_command = [
        "sbatch",
        # Slurm job specifications
        "-A", conf.ALLOCATION,
        "-p", conf.PARTITION,
        "-N", "1",
        "--cpus-per-task", str(conf.QUAST_CPUS),
        "-t", conf.QUAST_TIME,
        "-J", conf.QUAST_JOB_NAME,
        "--output", conf.QUAST_OUTPUT_LOG,
        "--error", conf.QUAST_ERROR_LOG,
        # The script to run
        conf.QUAST_SLURM_PATH,
        # Arguments to the slurm script
        conf.QUAST_CONTAINER_PATH,
        conf.RESULTS_PATH,
        conf.QUAST_ASSEMBLY_DIR
    ]
    
    # Submit the job
    try:
        subprocess.run(quast_command, check=True)
        print("QUAST job submitted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error submitting QUAST job: {e}")

# ----------[MAIN SCRIPT]----------
def main():
    """!
    @brief: Main function to orchestrate HPC job submissions.
    
    @details: Calls functions to submit various HPC jobs as needed. uses argparse
              to handle command-line arguments for flexibility.
    
    """
    parser = argparse.ArgumentParser(description="HPC Job Orchestrator")
    parser.add_argument(
        "--kraken2",
        action="store_true",
        help="Submit Kraken2 classification job"
    )
    parser.add_argument(
        "--flye",
        action="store_true",
        help="Submit Flye assembly job"
    )
    parser.add_argument(
        "--quast",
        action="store_true",
        help="Submit QUAST analysis job"
    )
    
    args = parser.parse_args()
    
    if args.kraken2:
        submit_kraken2_job()
    
    if args.flye:
        submit_flye_job()
    
    if args.quast:
        submit_quast_job()

    else:
        print("No jobs specified for submission. Use --kraken2, --flye, or --quast.")
    

if __name__ == "__main__":
    main()