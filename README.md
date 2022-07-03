# Bioinformatics Gene Sequencing Application

In bioinformatics many problems consist of determining how the structures of genes align using a scoring matrix. This match up allows us to infer the gene's functions. 

Created by Connor Dye as a California Polytechnic University Project.

## main.py Features
- Usage: given two strings which consists of DNA nucleic acids (A for adenine, T for thymine, etc) the application will display the gene alignment with the highest score
- program accepts as a command line argument the name of a file containing the two genes as strings and a
scoring matrix. Program will print to stdout the highest scoring alignment according to the following format: **1.)** The first given string, assumed to be x, will be printed above the second given string, assumed to be y and **2.)** The columns of the alignment will be space-separated, and ‘-’ characters are used to represent spaces within the aligned strings
-program utilizes the bioinformatics dynamic programming Needleman–Wunsch algorithm


## Notes
- program supports genes passed in as strings with nucleic acids A, C, G, T, "-"
- scoring matrix consists of 5 rows and 5 columns
- the scoring matrix may give value to certain base pairs that aren't exact matches, but that hold some sort of value (e.g A matched with T may be given some value as it may signify a mutation in a gene)
