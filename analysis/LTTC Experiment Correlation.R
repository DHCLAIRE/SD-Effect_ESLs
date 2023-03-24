library(dplyr)
library(tidyr)
library(lme4)
library(MASS)       # for boxcox(), contr.sdif
library(plyr)       # for ddply()
library(lmerTest)
library(Rmisc)
library(ggplot2)

rm(list = ls())
setwd("/Users/neuroling/Downloads/DINGHSIN_Results/2nd_Stim-results_selfPRT_PLDT/R_LMM_Analysis_Hsu")

# import data, keep strings as strings
data <- read.csv("000_007-036_PLDT_raw_results.csv", stringsAsFactors = F)

# remove data$ACC == 99
data = data[!(data$ACC == 99),]

# create a new column "novality", at the end of the whole data
data$novality <- data$Condition

# rename elements: "C"="NEW", "L"&"H"="OLD"
data[!(data$Condition == "C"), "novality"] = "OLD"
data[(data$Condition == "C"), "novality"] = "NEW"    

# make a copy of data
data_novality = data

# factor-ize nominal variables 
cols = names(data_novality)[c(1, 4, 9)]
cols
data_novality[cols] <- lapply(data_novality[cols], factor) 
contrasts(data_novality$novality)

## summary
data.novality.ACC<-summarySE(data=data_novality, measurevar="ACC",groupvars=c("novality","Sub_id"),
                     na.rm=T,conf.interval=0.95)
data.novality.RT<-summarySE(data=data_novality, measurevar="RT",groupvars=c("novality","Sub_id"),
                   na.rm=T,conf.interval=0.95)
data.novality.RT
data.novality.ACC

# remove data$Condition == C
data = data[!(data$Condition == "C"),]

# factor-ize nominal variables 
cols = names(data)[c(1, 2, 4)]
data[cols] <- lapply(data[cols], factor) 
contrasts(data$Condition)

## summary
data.CD.ACC<-summarySE(data=data, measurevar="ACC",groupvars=c("Condition","Sub_id"),
                             na.rm=T,conf.interval=0.95)
data.CD.RT<-summarySE(data=data, measurevar="RT",groupvars=c("Condition","Sub_id"),
                            na.rm=T,conf.interval=0.95)
data.CD.ACC
data.CD.RT

subj_table1 = reshape(data.CD.ACC[,c("Sub_id", "Condition", "ACC")], idvar = "Sub_id", timevar = "Condition", direction = "wide")
subj_table2 = reshape(data.CD.RT[,c("Sub_id", "Condition", "RT")], idvar = "Sub_id", timevar = "Condition", direction = "wide")
subj_table3 = reshape(data.novality.ACC[,c("Sub_id", "novality", "ACC")], idvar = "Sub_id", timevar = "novality", direction = "wide")
subj_table4 = reshape(data.novality.RT[,c("Sub_id", "novality", "RT")], idvar = "Sub_id", timevar = "novality", direction = "wide")

subj_table = cbind(subj_table1, subj_table2[,c(2, 3)], subj_table3[,c(2, 3)], subj_table4[,c(2, 3)])

cor(subj_table[,c(-1)])

# install.packages("psych")
library(psych)

pairs.panels(subj_table[,c(-1)],
             smooth = TRUE,      # If TRUE, draws loess smooths
             scale = FALSE,      # If TRUE, scales the correlation text font
             density = TRUE,     # If TRUE, adds density plots and histograms
             ellipses = TRUE,    # If TRUE, draws ellipses
             method = "pearson", # Correlation method (also "spearman" or "kendall")
             pch = 21,           # pch symbol
             lm = FALSE,         # If TRUE, plots linear fit rather than the LOESS (smoothed) fit
             cor = TRUE,         # If TRUE, reports correlations
             jiggle = FALSE,     # If TRUE, data points are jittered
             factor = 2,         # Jittering factor
             hist.col = 4,       # Histograms color
             stars = TRUE,       # If TRUE, adds significance level with stars
             ci = F,          # If TRUE, adds confidence intervals
             cex = 6)
