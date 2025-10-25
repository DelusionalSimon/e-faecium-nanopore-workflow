#!/bin/bash

#------------------------------------
#
#@file      01_kraken2.slurm
#@author    Simon Håkansson
#@date      2025-10-24
#@brief     This slurm script runs kraken2 using user input
#
# ------------------------------------


# ----------[SETUP]----------
# Paths
CONTAINER_PATH=$1
DB_PATH=$2
DATA_PATH=$3
RESULTS_PATH=$4

# Input
FILTERED_FASTQ_FILE=$5

# Outputs
KRAKEN_OUTPUT = $6
KRAKEN_REPORT = $7
KRAKEN_CLASSIFIED_FASTQ = $8
KRAKEN_UNCLASSIFIED_FASTQ = $9


# Bind paths for container
export SINGULARITY_BINDPATH="${DB_PATH}:/db,${DATA_PATH}:/data,${RESULTS_PATH}:/results"

# Create results directory
mkdir -p ${RESULTS_PATH}


# ----------[RUN KRAKEN2]----------

# Run Kraken2 classification
singularity exec ${CONTAINER_PATH} kraken2 \
        --db /db \
        --threads ${SLURM_CPUS_PER_TASK} \
        --output /results/${KRAKEN_OUTPUT} \
        --report /results/${KRAKEN_REPORT} \
        --classified-out /results/${KRAKEN_CLASSIFIED_FASTQ} \
        --unclassified-out /results/${KRAKEN_UNCLASSIFIED_FASTQ}\
        /data/${FILTERED_FASTQ_FILE} 
