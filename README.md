# SD-Effect_ESLs
This repository contains scripts and instructions to reproduce the results from the future manuscript *SD effect on ELs*  
Script authors:  
- R(LMM): [Dr. Chun-Hsien Hsu](https://github.com/deltaphase)  
- Python: [Ting-Hsin Yen](https://github.com/DHCLAIRE)


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
1. `form_LMMdata.py`: Produce the suitable form of data for LMM
2. `CD effect Stats LMM.R`: Showing figures and stats of CD effect
3. `Novality effect Stats LMM.R`: Showing figures and stats of Old-New effect
4. `Correlation.R`: Showing figures and stats of related correlations

