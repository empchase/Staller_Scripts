.PHONY : all settings help

READONE=$(wildcard *R1_001.fastq.gz)
READTWO=$(wildcard *R2_001.fastq.gz)
RESULTS=$(patsubst %_R1_001.fastq.gz,results/%.fastq.gz,$(READONE))

all : $(RESULTS)

results/%.fastq.gz : %_R1_001.fastq.gz %_R2_001.fastq.gz 
	bash pear.sh $< $(word 2,$^) $@

redo : 
	rm -f $(RESULTS)
	rm temp/*

clean : 
	rm temp/*

help :
	@echo This make file goes in the projects root directory
	@echo Needs 1 subdirectory, results
	@echo needs fastq.gz format reads
	@echo command make redo will remove results
	@echo command make clean will remove temp files
	@echo command make settings will show you what is detected

settings : 
	@echo READONE: $(READONE)
	@echo READTWO: $(READTWO)
	@echo RESULTS: $(RESULTS)
