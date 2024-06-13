#!/usr/bin/env bash
#Author: empchase@berkeley.edu

#SBATCH --job-name=pear
#
# Account:
#SBATCH --account=fc_mvslab
# Partition:
#SBATCH --partition=savio2
#
# Wall Clock Limit:
#SBATCH --time=48:00:00
## Commands to run:

readone=$1
readtwo=$2
result=$3

module load pear

pear -f $readone -r $readtwo -o $result -p 0.001
