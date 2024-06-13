#!/usr/bin/env bash
#Author: empchase@berkeley.edu

#SBATCH --job-name=mapper
#
# Account:
#SBATCH --account=fc_mvslab
# Partition:
#SBATCH --partition=savio2
#
# Wall Clock Limit:
#SBATCH --time=00:05:00
## Commands to run:

module load python

python3 step1mapper.py -i /global/scratch/users/empchase/CiberVII/CiberVII_CZB/shortSCU.txt -o test3raw_tinierCiberv2seq.csv -d /global/scratch/users/empchase/A10_sequencing/v2/a10_designfile.csv
