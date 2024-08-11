# Nanopore sequencing from protozoa to phages

Introduction
Welcome to the GitHub repository for our paper titled "Nanopore sequencing from protozoa to phages: decoding biological information on a string of biochemical molecules into human-readable signals". This repository contains the code and data used in our study, where we explored the efficacy of nanopore sequencing technology in decoding biological information from dynamic and hypervariable genomes, particularly in metagenomic samples that pose significant challenges for traditional short-read sequencing methods.

In this study, we focused on sequencing blood and fecal samples from mice infected with Trypanosoma brucei, a unicellular protozoan known for its hypervariable regions, which contribute to its ability to evade host immunity. We demonstrated that nanopore sequencing, with its long-read capabilities, is particularly effective in capturing and assembling these dynamic genomic regions. The results highlight the potential of nanopore sequencing in the taxonomic classification and de novo assembly of complex genomes in metagenomic contexts.

Preprint link:
https://www.biorxiv.org/content/10.1101/2024.08.04.606558v1.full

Repository Contents
This repository is structured to provide all the necessary resources for replicating the analyses presented in our paper. Below is an overview of the contents:

1. Code
Graph_Codes/: This directory contains all the scripts used for visualizing the raw nanopore data, taxonomic classification, and de novo assembly of the reads. 

2. Results
Graph_Codes/: Contains the graphical results, including the proportion of reads identified as Trypanosoma brucei and other organisms.

Getting Started
Prerequisites
To run the analyses, you will need the following software installed on your system:

R v.3.6.0
Python v.3.12.1
Matplotlib v.3.8.0
pandas v.2.2.0
seaborn v.0.13.1
Flye v2.9.2
MUMmer v4.0+
Assemblytics
MinKNOW v.22.05.5
EPI2ME-labs v2.9.2

Contributing
We welcome contributions from the community! Please feel free to open an issue or submit a pull request if you have any suggestions or improvements.

License
This repository is licensed under the GNU GPL License. See the LICENSE file for details.

Contact
For questions or inquiries about the study, please contact [jinenstar@gmail.com].

We hope this repository serves as a valuable resource for researchers interested in nanopore sequencing and metagenomic analysis. Thank you for your interest in our work!
