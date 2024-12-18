# GNN4siRNA
GNN approach to face with the problem of siRNA-mRNA efficacy prediction.

This repository provides the source code for "A graph neural network approach for the analysis of siRNA-target biological networks".

- The "**data**" Folder contains both "raw" and "processed" data. We reported three siRNA-mRNA interaction network datasets from 702 to 3518 interactions.

- The "**preprocessing**" folder contains five scripts we released for transforming raw data into the input of our model. It also includes a "params.py" file with paths of input files and other parameters.

- The "**model**" folder contains the main script "GNN4siRNA.py" for predicting siRNA-mRNA interactions. Once again, the "params.py" file contains all the parameters reported in the paper. Results of this script are given in terms of *Pearson correlation coefficient* and *mean squared error*.
