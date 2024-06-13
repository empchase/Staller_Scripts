import sys
import argparse
import re 
import warnings
import pandas as pd
import numpy as np
# import concurrent.futures
# import datetime
# import time

# duckdb_dir = '~/bin/duckdb'
# # Append the DuckDB directory to sys.path
# sys.path.append(duckdb_dir)

import duckdb
conn = duckdb.connect('/global/scratch/users/empchase/A10_sequencing/v2/analysis2.db') # connect to database with TBB map

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

def complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N', 'X':'X'} 
    bases = list(seq) 
    bases = [complement[base] for base in bases] 
    return ''.join(bases)
def reverse_complement(s):
        return complement(s[::-1])
    
    
def getmid(seq, pre, post, bclen):
    # seq = the sequence to parse
    # pre = substring that precedes piece of interest
    # post = substring that follows piece of interest
    # returns piece of interest

    # re_key = pre + "(.*)"+ post 
    # poi_search = re.search(re_key, seq)
    # if poi_search is None:
    #     #the barcode will be called X
    #     poi = "X"
        
    #     #then we search for which restriction site had the error
    #     #regex for the bc we want to ignore
    #     w = "(.{"+str(bclen)+"})" 
    #     pre_re = pre + w + "(.{7})"
    #     pre_search = re.search(pre_re, seq)
    #     post_re = "(\w{7})" + w + post
    #     post_search = re.search(post_re, seq)
        
    #     if pre_search is None and post_search is None:
    #         a = 'X'
    #         z = 'X'
    #     elif pre_search is None:
    #         poi = post_search.group(2)
    #         a = post_search.group(1)
    #         z = post
    #     elif post_search is None:
    #         poi = pre_search.group(1)
    #         z = pre_search.group(2)
    #         a = pre
    #     else:
    #         a = 'Z'
    #         z = 'Z'            
    # else:
    #     poi = poi_search.group(1)
    #     a = pre
    #     z = post
    
    # return poi, a, z

    re_key = pre + "(.*)"+ post
    poi_search = re.search(re_key, seq)
    if poi_search is None:
        poi = "X"
    else:
        poi = poi_search.group(1)
    
    return poi

#putative consensus sequences ***reverse complement of snapgene***
rpp = 'AGCGGCC' #7bp ; before rptr barcode in read1
rpf = 'CTCGAGT' #7 bp ; after rptr barcode in read1

# function to parse RPTR fastq
def rbc_finder(readfile, bc_pre=rpp, bc_post=rpf, bc_len=14, chunk_size=100000):
    #readfile = fastq file -- RPTR files are read1
    #default values for the pre/post regions defined in above cell
    
    # Initialize DataFrame
    BC_df = pd.DataFrame(columns=["BCs", "Length", "Library"])

    # # Initialize Chunk Counter
    # chunk_count = 0

    # Open file and read in chunks
    with open(readfile, 'r') as fin:
        while True:
            #print Chunk step
            # chunk_count += 1
            # print(chunk_count)

            # Read file in chunks
            lines = [next(fin) for _ in range(chunk_size)]
            if not lines:
                break


            # Process chunk: make lists of reads
            seqlist = []
            for line in lines:
                if line.startswith('@'):
                    #look at next line to get read sequence, add to list
                    seq = next(fin).strip()
                    seqlist.append(seq)


            # Process reads in the chunk - extract BCs
            for read in seqlist:
                # bc, prex, postx = getmid(read, bc_pre, bc_post, bc_len)
                bc = getmid(read, bc_pre, bc_post, bc_len)
                bc = reverse_complement(bc) #return reverse complement
                bcl = len(bc)

                # Add BC and BC_len to DF
                BC_df = BC_df.append({'BCs': bc, 'Length':bcl}, ignore_index=True)

    
    # #make lists of BCs from list of reads
    # bc_list = []
    # bc_lens = []       
    # for read in seqlist:
    #     bc, prex, postx = getmid(read, bc_pre, bc_post, bc_len)
    #     bc = reverse_complement(bc) #return reverse complement
    #     bc_list.append(bc)
    #     bcl = len(bc)
    #     bc_lens.append(bcl)

    # #make the dict/df
    # BC_dict = {"BCs":bc_list, "Length":bc_lens} 
    # BC_df = pd.DataFrame.from_dict(BC_dict)
    
    #label df with library name
    libname = '_'.join(readfile.split('/')[-1].split('_')[0:6])
    BC_df['Library'] = libname
    
    return BC_df

# function that queries TBB table with a RPTRbc, returns the corresponding TBB, and inserts that TBB result into an empty list
def RPTR_SQLsearch(query):
    try:
        myquery = conn.sql("SELECT AD, AD_BC FROM A10_2_T_NODBLMAP_20240422 WHERE RPTR_BC='{}'".format(query)).to_df() #search for corresponding Tile-ADbc
        myquery ['AD_ADBC'] = myquery['AD'] + '-' +myquery['AD_BC'] # create a column that puts together ADs+BCs
        ptb = list(set(myquery ['AD_ADBC'].to_list())) #make a list out of that column and remove duplicates
        
        if not ptb:
            ptb = 0
        else:
            pass
#         print(len(ptb))

    except KeyError:
        ptb = 0

    return ptb #return the list of potential ADBCs 


#function to analyze reads
def SQLanalyze_tiles_rptrbcs (df, bc_len=14):
    # df = barcode containing df, parsed from fastq
    # bc_len = int, expected barcode length
    # tbb_dictkey = str, either 'ADbc' or 'RPTRbc'
    
    print(df.loc[0,'Library'])

    tr = df.shape[0] #total reads
    print(f'Total Reads {tr}')
    
    cls = df[(df['Length']== bc_len)] #cl = correct length
    print('Reads w BC and Tile of correct length')
    clcount = cls.shape[0]
    print(clcount)
    
    print('% Reads w correct length BCs')
    clpct = cls.shape[0]/df.shape[0]
    print (clpct)
    
    #df of BC coverage
    cl_covdf = cls['BCs'].value_counts().to_frame().reset_index() 
    print('# Unique RPTR BCs')
    uniqbccount = cl_covdf.shape[0]
    print(uniqbccount)
    print('SUM Unique BCs')
    print(cl_covdf.sum(numeric_only=True)['BCs'])

    #copy down unique BCs into a list
    bcs = cl_covdf['index'].tolist()
    


    matchlist = [] #list of TBBs that match the BCs

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = executor.map(RPTR_SQLsearch, bcs)
    #     for r in results:
    #         matchlist.append(r)

    for x in bcs:
        myquery = RPTR_SQLsearch(x)
        matchlist.append(myquery)

            
    cl_covdf['PutativeTileADBC'] = matchlist
    
    matchesonly = cl_covdf.replace(0, np.nan)
    matchesonly = matchesonly.dropna()
    totmatches = matchesonly.sum(numeric_only=True)['BCs']
    print('# BC matches to A10 deep seq map (Thresholded)')
    mapmatches = matchesonly.shape[0]
    print(mapmatches)
    
    print('TOT BC matches to A10 deep seq map')
    print(totmatches)
    
#     print('% unique BCs matched')
#     print(totmatches/cl_covdf.shape[0])
    
    
    print()
    
    #label the df with library name
    
    libname = df.loc[0,'Library']
    matchesonly['Library'] = libname
    
    statslist = [libname, tr, clcount, clpct, uniqbccount, mapmatches, totmatches]
    print(statslist)
    
    return matchesonly
    

# set up main code to be run
def main(input_file, output_file):

    # process input file into  df
    rawmap = rbc_finder(input_file)

    # Filter raw df 
    countsdf = SQLanalyze_tiles_rptrbcs(rawmap)


    # write the output file to csv
    countsdf.to_csv(output_file)





if __name__ == "__main__":
    # Check if the script is being run as the main program

    # Create ArgumentParser object with a description
    parser = argparse.ArgumentParser(description='Build Tile-BC map from step1 fastq file')

    # Add arguments to the parser
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    # Add an argument for the input file path. -i or --input specifies the argument name.
    # It's required (required=True), of type string (type=str), and has a help message.

    parser.add_argument('-o', '--output', type=str, required=True, help='Raw data output file path')
    # Add an argument for the output file path. -o or --output specifies the argument name.
    # It's required (required=True), of type string (type=str), and has a help message.

    # parser.add_argument('-c', '--clean_output', type=str, required=True, help='Clean data output file path')
    # # Add an argument for the output file path. -o or --output specifies the argument name.
    # # It's required (required=True), of type string (type=str), and has a help message.

    # parser.add_argument('-d', '--design', type=str, required=True, help='Design file (each line in file is a designed tile) path')
    # # Add an argument for the output file path. -o or --output specifies the argument name.
    # # It's required (required=True), of type string (type=str), and has a help message.

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args.input, args.output)
    conn.close()