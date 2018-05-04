#!/bin/bash
#SBATCH --job-name=lefors-nextflow-test
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --output=nextflow_test.out
#SBATCH --error=lefors-next_text.err
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=6
module add nextflow
module add python3
module add java

nextflow run nf_process.nf

