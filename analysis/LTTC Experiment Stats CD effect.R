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

# remove data$Condition == C
data = data[!(data$Condition == "C"),]

# factor-ize nominal variables 
cols = names(data)[c(1, 2, 4)]
data[cols] <- lapply(data[cols], factor)
contrasts(data$Condition)

## effect coding
# novality (1=H,-1=L)
data$Condition<-factor(data$Condition,levels=c("H","L"))
contrasts(data$Condition)<-contr.sum(2)
contrasts(data$Condition)

data$ACC <- as.numeric(data$ACC)
data$RT <- as.numeric(data$RT)

# fit glmer models with ACC
m.0<-glmer(ACC~Condition*Times*Trials+(1|Sub_id)+(1|Item),
            family=binomial,control=glmerControl(optimizer="bobyqa"),
            data=data)

m.1<-glmer(ACC~Condition*Times*Trials - Condition:Times:Trials+(1|Sub_id)+(1|Item),
            family=binomial,control=glmerControl(optimizer="bobyqa"),
            data=data)

# fit glmer models with ACC
m.0<-glmer(ACC~Condition*Times*Trials+(1|Sub_id)+(1|Item),
           family=binomial,control=glmerControl(optimizer="bobyqa"),
           data=data)

m.1<-glmer(ACC~Condition*Times*Trials - Condition:Times:Trials+(1|Sub_id)+(1|Item),
           family=binomial,control=glmerControl(optimizer="bobyqa"),
           data=data)

# no difference between m.0 and m.1, so drop the highest interaction
anova(m.0, m.1)

# do not need two-way interactions either
drop1(m.1, test = c("Chisq"))


m.2<-glmer(ACC~Condition + Times + Trials +(1|Sub_id)+(1|Item),
           family=binomial,control=glmerControl(optimizer="bobyqa"),
           data=data)

# significant effect of Condition
drop1(m.2, test = c("Chisq"))

m.3<-glmer(ACC~Condition+(1|Sub_id)+(1|Item),
           family=binomial,control=glmerControl(optimizer="bobyqa"),
           data=data)
summary(m.3)
# H-L: b=0.22, S.E. = 0.064, z = 3.541, p < .001

## summary
data.mean<-summarySE(data=data, measurevar="ACC",groupvars=c("Condition","Sub_id"),
                     na.rm=T,conf.interval=0.95)
data.mean<-summarySE(data=data.mean,measurevar="ACC",groupvars=c("Condition"),
                     na.rm=T,conf.interval=0.95)
data.mean

g<-ggplot(data.mean, aes(x=Condition, y=ACC, fill=Condition))+
  geom_bar(position=position_dodge(),stat="identity",fill=c("#E69F00","#56B4E9"),
           colour="black", # Use black outlines
           size=.3)+ # Thinner lines
  geom_errorbar(aes(ymin=ACC-se,ymax=ACC+se),
                width=.2,
                position=position_dodge(.9))+
  xlab("Contextual Diversity")+
  ylab("Accuracy")+
  coord_cartesian(ylim=c(0.5, 1))+
  theme_set(theme_bw(base_size=12))
g




# remove incorrect trials 
data = data[(data$ACC==1),]

# fit lmer models with RT
m.0 <- lme4::lmer(RT ~ Condition*Times*Trials + 
                    (1|Sub_id)+(1|Item),
                  data = data, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))

m.1 <- lme4::lmer(RT ~ Condition*Times*Trials -Condition:Times:Trials + 
                    (1|Sub_id)+(1|Item),
                  data = data, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))
# no difference between m.0 and m.1, so drop the highest interaction
anova(m.0, m.1)

# drop two-way interaction
drop1(m.1, test = c("Chisq"))

m.2 <- lme4::lmer(RT ~ Condition + Times + Trials +
                  (1|Sub_id)+(1|Item),
                  data = data, REML = FALSE,
                  control=lmerControl(optimizer="bobyqa"))

# no significant effect
drop1(m.2, test = c("Chisq"))

## summary and plot
data.mean<-summarySE(data=data, measurevar="RT",groupvars=c("Condition","Sub_id"),
                   na.rm=T,conf.interval=0.95)
data.mean<-summarySE(data=data.mean,measurevar="RT",groupvars=c("Condition"),
                   na.rm=T,conf.interval=0.95)
data.mean

g<-ggplot(data.mean, aes(x=Condition, y=RT, fill=Condition))+
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
