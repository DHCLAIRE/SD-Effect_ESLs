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
getwd()

# import data, keep strings as strings
data <- read.csv("000_007-036_PLDT_raw_results.csv", stringsAsFactors = F)

# remove data$ACC == 99
data = data[!(data$ACC == 99),]

# create a new column "novality"
data$novality <- data$Condition
data

# rename elements: "C"="NEW", "L"&"H"="OLD"
data[!(data$Condition == "C"), "novality"] = "OLD"
data[(data$Condition == "C"), "novality"] = "NEW"
data

# make a copy of data
data_novality = data
data_novality

# factor-ize nominal variables
cols = names(data_novality)[c(1, 4, 9)]
cols
data_novality[cols] <- lapply(data_novality[cols], factor)
data_novality[cols]
contrasts(data_novality$novality)


## effect coding
# novality (1=OLD,-1=NEW)
data_novality$novality<-factor(data_novality$novality,levels=c("OLD","NEW"))
contrasts(data_novality$novality)<-contr.sum(2)
contrasts(data_novality$novality)

data_novality$ACC <- as.numeric(data_novality$ACC)

# fit glmer models with ACC
m.0<-glmer(ACC~novality*Times*Trials+(1|Sub_id)+(1|Item),
            family=binomial,control=glmerControl(optimizer="bobyqa"),
            data=data_novality)

m.1<-glmer(ACC~novality*Times*Trials - novality:Times:Trials+(1|Sub_id)+(1|Item),
            family=binomial,control=glmerControl(optimizer="bobyqa"),
            data=data_novality)

# no difference between m.0 and m.1, so drop the highest interaction
anova(m.0, m.1)

# do not need two-way interactions either
drop1(m.1, test = c("Chisq"))


m.2<-glmer(ACC~novality + Times + Trials +(1|Sub_id)+(1|Item),
           family=binomial,control=glmerControl(optimizer="bobyqa"),
           data=data_novality)

# no significant effect
drop1(m.2, test = c("Chisq"))
summary(m.2)


## summary
data.mean<-summarySE(data=data_novality, measurevar="ACC",groupvars=c("novality","Sub_id"),
                     na.rm=T,conf.interval=0.95)
data.mean<-summarySE(data=data.mean,measurevar="ACC",groupvars=c("novality"),
                     na.rm=T,conf.interval=0.95)
data.mean

g<-ggplot(data.mean, aes(x=novality, y=ACC, fill=novality))+
  geom_bar(position=position_dodge(),stat="identity",fill=c("#E69F00","#56B4E9"),
           colour="black", # Use black outlines
           size=.3)+ # Thinner lines
  geom_errorbar(aes(ymin=ACC-se,ymax=ACC+se),
                width=.2,
                position=position_dodge(.9))+
  xlab("Novality")+
  ylab("Accuracy")+
  coord_cartesian(ylim=c(0.5, 1))+
  theme_set(theme_bw(base_size=12))
g






# remove incorrect trials 
data_novality = data_novality[(data_novality$ACC==1),]

# fit lmer models with RT
m.0 <- lme4::lmer(RT ~ novality*Times*Trials + 
                    (1|Sub_id)+(1|Item),
                  data = data_novality, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))

m.1 <- lme4::lmer(RT ~ novality*Times*Trials - novality:Times:Trials + 
                    (1|Sub_id)+(1|Item),
                  data = data_novality, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))
# no difference between m.0 and m.1, so drop the highest interaction
anova(m.0, m.1)

# drop two-way interaction
drop1(m.1, test = c("Chisq"))

m.2 <- lme4::lmer(RT ~ novality + Times + Trials +
                  (1|Sub_id)+(1|Item),
                  data = data_novality, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))

# keep "novality"
drop1(m.2, test = c("Chisq"))

m.3 <- lme4::lmer(RT ~ novality +
                    (1|Sub_id)+(1|Item),
                  data = data_novality, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))
summary(m.3)
m.3 %>% as_lmerModLmerTest() %>% anova(type = c("III"),ddf = c("Satterthwaite"))
# OLD-NEW: -67.077 ms (S.E. = 9.006) [F = 55.473, p < .0001]

## summary and plot
data.mean<-summarySE(data=data_novality, measurevar="RT",groupvars=c("novality","Sub_id"),
                   na.rm=T,conf.interval=0.95)
data.mean<-summarySE(data=data.mean,measurevar="RT",groupvars=c("novality"),
                   na.rm=T,conf.interval=0.95)
data.mean

g<-ggplot(data.mean, aes(x=novality, y=RT, fill=novality))+
  geom_bar(position=position_dodge(),stat="identity",fill=c("#E69F00","#56B4E9"),
           colour="black", # Use black outlines
           size=.3)+ # Thinner lines
  geom_errorbar(aes(ymin=RT-se,ymax=RT+se),
                width=.2,
                position=position_dodge(.9))+
  xlab("Novality")+
  ylab("Response Time (ms)")+
  coord_cartesian(ylim=c(500, 1200))+
  theme_set(theme_bw(base_size=12))
g
