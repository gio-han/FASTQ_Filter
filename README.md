# Next Generation Sequencing (NGS) FASTQ File Filter


## Description of the Project

When DNA sequences are produced on a sequencer a measure of quality is required. This quality score is called the Q value and is assigned to each base as it is predicted.

This Python script reads Next-Generation Sequencing (NGS) files in the FASTQ format and filters out paired end reads according to their average quality scores. "Paired end reads" means that each DNA fragment is sequenced from both ends. The script outputs two files. The first contains the sequences where both reads have an average score above and including, 30 and the second those sequences that have at least 1 read with an average score below 30.

The FASTQ file named 'seq_sample.fastq' in the same repository can be used as an example file to test the script.


## Key Features

* Q-score Threshold: Filters reads based on an average quality score of 30.
* Categorized Outputs: Generates two output files:
  * Sequences with both reads meeting the quality threshold.
  * Sequences with at least one read below the quality threshold.


## Installations

Python 3 is required but no other packages or libraries are needed.
