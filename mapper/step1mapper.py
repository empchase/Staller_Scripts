# import packages

import re
import pandas as pd
import time

# define needed functions for data processing

def find_designed(des):
    """ takes a file where every line is a designed tile and creates a lookup dictionary of all designed tiles """
    dt = [] # initialize a list of designed tiles from design file
    with open(des, 'r') as f_des:
        # open the design file for reading
        for line in f_des:
            if "ArrayDNA" in line: #skip the "arrayDNA" line if applicable
                pass
            else:
                dt.append(line.strip()) #add tile to list without whitespace
    
    dt_dict = {} # initialize dictionary to lookup tiles in
    for i in dt:
        dt_dict[i] = 1 # add tiles into a diction ary
        
    print('Number of designed tiles:', len(dt_dict)) 

    return dt_dict


def tilebc_mapper(read, design_dict,
                  ad_preceder = "GGCTAGC", ad_length = 120, 
                  bc1_preceder = "CGCGCC", bc1length = 11): #editted for no RPTR bc
    """
    read: (str) line in fastq/read file with DNA sequence 
    ad_preceder: 7 bp upstream (5') of the tile/AD
    ad_length: length of tile
    bc1_preceder: 7 bp upstream (5') of the AD barcode
    bc1_length: length of AD BC
    """
    
    #Initial ad search
    searched_read = re.split(ad_preceder, read, maxsplit=1) 
    AD = None
    barcode1 = None
    designed = 0
    
    if len(searched_read) == 2: #if the first ad search was successful
        roi = searched_read[1] #then take the ad search
        AD = roi[:ad_length] #and save the AD as the first part of the string
        
        #Check if AD Tile was designed
        if design_dict:
            if AD in design_dict:
                designed = 1
        
        #Initial bc1 search
        searched_read = re.split(bc1_preceder, roi[ad_length:], maxsplit=1) #look for the barcode using the bc preceder in the portion of the read beyond the AD
        if len(searched_read) == 2: #if initial bc1 search was successful
            barcode1 = searched_read[1][:bc1length] #then the barcode is the first 11 characters of the search result
        else: #if bc search via preceder was unsuccessful
            #Secondary bc1 search
            barcode1 = roi[139:150]
    #         print(len(barcode))
    
    return AD, barcode1, designed

def buildmapdf (readfile, tbm_design_dict):

    """
    readfile: fastq file   
    tbm_design_dict: output of find_designed()
    """
    
    total_designed = 0 #to immediately count how many tiles were designed
    # start1 = time.perf_counter() #start counter
    
    data = []
    
    with open(readfile, 'r') as fin:
        print("Opened file")

        for line in fin:
            if line.startswith('@'):
                seq = next(fin) # look at next line to get read sequence, add to list
                seq = seq.strip() # clean the read

                #find ad tile and bcs
                to_df = tilebc_mapper(seq, tbm_design_dict) 
                #count the number of designed
                total_designed += to_df[2]

            data.append(to_df)
        
    # finish = time.perf_counter()
    # print(f'finished processing in {round(finish-start1, 2)} seconds')
    
    print(f'Total designed = {total_designed}')
    # print(f'Total designed = {total_designed} out of {total_iterations}')
#     print(data)
    output_df = pd.DataFrame(data, columns=['AD', 'AD_BC', 'Designed'])
    # finish = time.perf_counter()
    # print(f'finished creating df in {round(finish-start1, 2)} seconds')
    return output_df


# set up main code to be run

def main(input_file, output_file, design_file):
    # get list of designed tiles
    designed_tile_dictionary = find_designed(design_file)

    # process input file into raw df
    rawmap = buildmapdf(input_file, designed_tile_dictionary)

    # write the output file
    rawmap.to_csv(output_file)


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

    parser.add_argument('-d', '--design', type=str, required=True, help='Design file (each line in file is a designed tile) path')
    # Add an argument for the output file path. -o or --output specifies the argument name.
    # It's required (required=True), of type string (type=str), and has a help message.

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args.input, args.output, args.design)