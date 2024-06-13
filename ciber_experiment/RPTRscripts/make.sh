#!/usr/bin/env bash
#Author: empchase@berkeley.edu

#SBATCH --job-name=RPTRreadsmapper
#
# Account:
#SBATCH --account=fc_mvslab
# Partition:
#SBATCH --partition=savio2_bigmem
#
# Wall Clock Limit:
#SBATCH --time=24:00:00

#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=empchase@berkeley.edu

## Commands to run:

module load python

make -f Makefile all
