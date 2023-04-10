# SD-Effect_ESLs
This repository contains scripts and instructions to reproduce the results from the manuscript *SD effect on ELs*

# Setup
## Step 1: Download this repository
Option 1: Clone this repository  
Option 2: Simply download it as a zip file.


## Step 2: Prepare your materials (texts & Pseudowords)
1. `Read materials_MacOS-Linux.py`: Load in the modified texts
2. `TextStim_MacOS-Linux.py`: Split pseudowords, categorize text sets...??

## Step 3: Conduct your experiments
#### MacOX version
1. `Reading_MacOS-Linux_ver.py`: Reading 30 texts + reading comprehension rating (Training phase)
2. `LDT_MacOS-Linux_ver.py`: Pseudoword Lexical Decision Task (PLDT) (Evaluation phase)
#### Windows 10 version
1. `Reading_Windows_ver.py`: Reading 30 texts + reading comprehension rating (Training phase)
2. `LDT_Windows_ver.py`: Pseudoword Lexical Decision Task (PLDT) (Evaluation phase)

## Step 4: Use Linear Mix Model (LMM) to analyze the results
1. `form_LMMdata.py`: Produce the suitabl form of data for LMM
2. `CD effect Stats LMM.R`: Showing figures and stats of CD effect
3. `Novality effect Stats LMM.R`: Showing figures and stats of Old-New effect
4. `Correlation.R`: Showing figures and stats of related correlations





## Below is the Example Instructions from [Eelbrain/Alice](https://github.com/Eelbrain/Alice)
# Alice dataset for Eelbrain
This repository contains scripts and instructions to reproduce the results from the manuscript Eelbrain: A toolkit for time-continuous analysis with temporal response functions.

# Setup
Download this repository
If you're familiar with git, clone this repository. If not, simply download it as a zip file.

# Create the Python environment
The easiest way to install all the required libraries is with conda, which comes with the Anaconda Python distribution. Once conda is installed, simply run, from the directory in which this README file is located:

$ conda env create --file=environment.yml
This will install all the required libraries into a new environment called eelbrain. Activate the new environment with:

$ conda activate eelbrain
You will have to activate the environment every time you start a new shell session.

# Download the Alice dataset
Download the Alice EEG dataset. This repository comes with a script that can automatically download the required data from UMD DRUM by running:

$ python download_alice.py
The default download location is ~/Data/Alice. The scripts in the Alice repository expect to find the dataset at this location. If you want to store the dataset at a different location, provide the location as argument for the download:

$ python download_alice.py download/directory
then either create a link to the dataset at ~/Data/Alice, or change the root path where it occurs in scripts (always near the beginning).

This data has been derived from the original dataset using the script at import_dataset/convert-all.py.

# Download TRFs
All TRFs used in the different figures can be computed and saved using the scripts in the analysis directory. However, this may require substantial computing time. To get started faster, the TRFs can also be downloaded from here. Just move the downloaded TRFs folder into the ~/Data/Alice directory, i.e., as ~/Data/Alice/TRFs.

# Notebooks
Many Python scripts in this repository are actually Jupyter notebooks. They can be recognized as such because of their header that starts with:

# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
These scripts were converted to Python scripts with Jupytext for efficient management with git. To turn such a script back into a notebook, run this command (assuming the script is called notebook.py):

$ jupytext --to notebook notebook.py
Subdirectories
Predictors
The predictors directory contains scripts for generating predictor variables. These should be created first, as they are used in many of the other scripts:

make_gammatone.py: Generate high resolution gammatone spectrograms which are used by make_gammatone_predictors.py
make_gammatone_predictors.py: Generate continuous acoustic predictor variables
make_word_predictors.py: Generate word-level predictor variables consisting of impulses at word onsets
Analysis
The analysis directory contains scripts used to estimate and save various mTRF models for the EEG dataset. These mTRF models are used in some of the figure scripts.

Figures
The figures directory contains the code used to generate all the figures in the paper.

Import_dataset
This directory contains the scripts that were used to convert the data from the original Alice EEG dataset to the format used here.

Further resources
This tutorial and dataset:

Ask questions
Report issues
Eelbrain:

Command reference
Examples
Ask questions
Report issues
Other libraries:

Matplotlib
MNE-Python

