#!/bin/bash

#------------------------------------
#
#@file      02_flye.slurm
#@author    Simon Håkansson
#@date      2025-10-25
#@brief     This slurm script runs flye using user input
#
# ------------------------------------

# ----------[SETUP]----------
CONTAINER_PATH=$1
DATA_PATH=$2
RESULTS_PATH=$3

# Input
FILTERED_FASTQ_FILE=$4

# Settings
ITERATIONS=$5

# Set bind paths for Singularity
export SINGULARITY_BINDPATH="${DATA_PATH}:/data,${RESULTS_PATH}:/results"

# Set output dirs
CONTAINER_OUTPUT_DIR="/results/flye"
REAL_OUTPUT_DIR="${RESULTS_PATH}/flye"

# Create output directory
mkdir -p ${OUTPUT_DIR}

# ----------[RUN FLYE]----------

# Run Flye assembly with enhanced polishing
singularity exec ${CONTAINER_PATH} flye --nano-raw /data/${FILTERED_FASTQ_FILE} \
     --out-dir ${REAL_OUTPUT_DIR} \
     --threads ${SLURM_CPUS_PER_TASK} \
     --iterations ${ITERATIONS} \
