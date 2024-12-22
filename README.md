## Juniperus-deppeana-complex-speciation
This repository contains the scripts that were used for the analysis of genetic diversity, genetic structure and to reconstruct phylogenetic relationships within the *Juniperus deppeana* complex. The scripts are part of the methods of the publication: 

### Nearly synchronic speciation in the Mexican highlands: Did the *Juniperus deppeana* complex diverged under peripatry?

Authors: Rodrigo Martínez de León, Melania Vega, David S. Gernandt, Juan Pablo Jaramillo-Correa, Alejandra Moreno-Letelier

Abstract:

### Data characteristics
- Genotype By Sequencing
- Paired-end reads
- PstI/MspI restriction enzyme
- Illumina NovaSeq 6000
#### Workflow and the necessary software
##### 1. Read cleaning and genomic variant calling
- Stacks v2
- FastQC
- TrimGalore v.0.6.10
- BWA 0.7.17
- Samtools 1.10
- Picard 2.6.2
- Qualimap v2.2.1
- NGSEP v4.3.1
- VCFtools
- Admixture
##### 2.Genetic structure and phylogenetic relationships
- snapper
- BEAST2
##### 3.Species delimitation
- DelimitR
- EasySFS
- fastsimcoal2 v2.7
##### 4.Divergence time estimation
- ABCToolbox
- fastsimcoal2 v2.7
