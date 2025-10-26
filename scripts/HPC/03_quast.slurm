#!/bin/bash

#------------------------------------
#
#@file      03_quast.slurm
#@author    Simon Håkansson
#@date      2025-10-26
#@brief     This slurm script runs QUAST using user input
#
# ------------------------------------

# ----------[SETUP]----------
CONTAINER_PATH=$1
RESULTS_PATH=$2

# Input
QUAST_ASSEMBLY_DIR=$3

# Output
OUTPUT_DIR="${RESULTS_PATH}/quast_results"

# Bind paths for container
export SINGULARITY_BINDPATH="${QUAST_ASSEMBLY_DIR}:/assembly,${OUTPUT_DIR}:/output"

# Create output directory
mkdir -p ${OUTPUT_DIR}

# ----------[RUN QUAST]----------
singularity exec ${CONTAINER_PATH} quast.py \
    -o ${OUTPUT_DIR} \
    --threads ${SLURM_CPUS_PER_TASK} \
    --plots-format png \
    /assembly/assembly.fasta \

echo "QUAST analysis completed"