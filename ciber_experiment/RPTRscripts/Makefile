# Define variables
INPUT_DIR := /global/scratch/projects/fc_mvslab/data/sequencing/CZB_Apr2024/20240425/EC_Ciber2/results/assembled_reads/RPTR_reads/notanalyzed
OUTPUT_DIR := /global/scratch/users/empchase/Ciber2_ii/analyzed_dfs/RPTR

# List of input files
INPUT_FILES := $(wildcard $(INPUT_DIR)/*.fastq)

# Define rules
all: $(patsubst $(INPUT_DIR)/%.fastq,%_output.csv,$(INPUT_FILES))

%_output.csv: $(INPUT_DIR)/%.fastq
	python3 RPTRreadsmapper.py -i $< -o $(OUTPUT_DIR)/$@ 

.PHONY: clean
clean:
	rm -f $(OUTPUT_DIR)/*.csv
