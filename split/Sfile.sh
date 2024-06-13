#!/bin/bash
## Replace MY_PI_SUNetID_or_Project_ID with the PI/project to be charged.

#SBATCH --account=fc_mvslab

## savio partitions are savio, savio_bigmem, savio2, savio2_bigmem, savio2_htc and ... 
#SBATCH --partition=savio2_bigmem

## Set job time to 24 hours
#SBATCH --time=24:00:00

## Set a name for the job, visible in `squeue`
#SBATCH --job-name="SepFiles"

## The following settings are optimal for *most* software, we want one task 
## to have one or more cores available for that task to fork or use threads.
## One node, -N also works
#SBATCH --nodes=1
## Number of tasks, -n also works. For 10x local mode use only 1 taks per node.
#SBATCH --ntasks=1 
## To take advantage of multi-threading, use 16 CPU/core per task, -c also works.
#SBATCH --cpus-per-task=1

## There are to ways to specify memory, --mem= and --mem-per-cpu= 
## --mem is usually enough since total job memory is easy to specify 
## this way.
#SBATCH --mem=128G 
    
## Open an job array for multiple runs
## Always remember to check the number here!!!
## The range of numbers to use for the array

## Specify log file location to help with better logging of errors/outputs.
#SBATCH -o CRcount-%A-%a.out
#SBATCH -e CRcount-%A-%a.err
##SBATCH --array=1-73
## Put any module here, anaconda environment example shown here:
## Modules needed for the pipeline to run

## Optionally activate environment
ml python
##SAMPLELIST=Sample_list0908.txt
##Outpath=/global/scratch/projects/fc_mvslab/data/sequencing/EKdata_pairReads/
##Datapath=/global/scratch/projects/fc_mvslab/data/sequencing/EKdata0908/
pip install Bio
python Sfiles.py
