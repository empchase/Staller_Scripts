#!/usr/bin/env bash
#Author: empchase@berkeley.edu

#SBATCH --job-name=ADreadsmapper
#
# Account:
#SBATCH --account=fc_mvslab
# Partition:
#SBATCH --partition=savio2
#
# Wall Clock Limit:
#SBATCH --time=08:00:00
## Commands to run:

module load python

make -f Makefile all