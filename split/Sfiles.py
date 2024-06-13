import os,sys,re
import gzip
from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import itertools
import argparse

ADid = 'GAAATTC'
RPTRid = 'TAATTAC'
path = '/global/scratch/users/empchase/CiberVII/CiberVII_CZB/'

def SeperateFiles(ad_or_rptr):
  with gzip.open(path + "SCU_Oct2023_S2_L004_R1_001.fastq.gz",'rt') as fh:
    print('file opened')
    lines = fh.readlines()
    E_set = []
    K_set = []
    for num, line in enumerate(lines):
      if num%4==1:
        if line.find(ad_or_rptr)!= -1:  #AD: GAAATTC #RPTR: TAATTAC 
          E_set.append(lines[num - 1])
          E_set.append(line)
          E_set.append(lines[num + 1])
          E_set.append(lines[num + 2])
        else:
          K_set.append(lines[num - 1])
          K_set.append(line)
          K_set.append(lines[num + 1])
          K_set.append(lines[num + 2])
  print('file parsed')

  E_handle = open(path+"RPTR_4_30_16X16_0927_S205_L004_R1_001_demultiplexed.fastq", "w")
  for line in E_set:
    E_handle.write(line)
  E_handle.close()
  print('EC file done')
      
  K_hundle = open(path+"SCU_Oct2023_S2_L004_R1_001_demultiplexed.fastq", "w")
  for line in K_set:
    K_hundle.write(line)
  K_hundle.close()
  print('K file done')


SeperateFiles(RPTRid)