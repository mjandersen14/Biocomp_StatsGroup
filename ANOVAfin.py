#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:41:28 2018

@author: Samuel_Clarin
"""

##import programs

import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from plotnine import *

#importing data

antibiotics=pd.read_csv("antibiotics.csv", header=0, sep=",")

#visualizing data

ggplot(antibiotics, aes(x="trt",y="growth"))+geom_boxplot()

#running ANOVA

ANOVA1=ols('growth ~ C(trt)', data=antibiotics).fit()
ANOVA1.summary()
ANOVA_table=sm.stats.anova_lm(ANOVA1, typ=2)
ANOVA_table

import pandas as pd
datafile = "PlantGrowth.csv"
data = pd.read_csv(datafile)
 
#Create a boxplot
antibiotics.boxplot('growth', by='trt')
 
ctrl = antibiotics['growth'][data.group == 'trt']
 
grps = pd.unique(data.group.values)
d_data = {grp:data['trt'][data.group == grp] for grp in grps}
 
k = len(pd.unique(data.group))  # number of conditions
N = len(data.values)  # conditions times participants
n = data.groupby('trt').size()[0] #Participants in each condition
DFbetween = k - 1
DFwithin = N - k
DFtotal = N - 1
SSbetween = (sum(data.groupby('trt').sum()['growth']**2)/n) \
    - (data['growth'].sum()**2)/N

sum_y_squared = sum([value**2 for value in data['growth'].values])
SSwithin = sum_y_squared - sum(data.groupby('trt').sum()['growth']**2)/n

SStotal = sum_y_squared - (data['growth'].sum()**2)/N

MSbetween = SSbetween/DFbetween



F = MSbetween/MSwithin

p = stats.f.sf(F, DFbetween, DFwithin)



