#!/usr/bin/env bash
#Author: empchase@berkeley.edu

#SBATCH --job-name=gzip
#
# Account:
#SBATCH --account=fc_mvslab
# Partition:
#SBATCH --partition=savio2
#
# Wall Clock Limit:
#SBATCH --time=02:00:00
## Commands to run:

gzip *.fastq
