#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:41:28 2018

@author: Samuel_Clarin
"""

##import programs

import pandas as pd
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
from plotnine import *

#importing data

sugar=pd.read_csv("sugar.csv", header=0, sep=",")
antibiotics=pd.read_csv("antibiotics.csv", header=0, sep=",")

#visualizing data

ggplot(antibiotics, aes(x="trt",y="growth"))+geom_jitter()

#running ANOVA

ANOVA1=ols('growth ~ C(trt)', data=antibiotics).fit()
ANOVA1.summary()
ANOVA_table=sm.stats.anova_lm(ANOVA1, typ=2)
ANOVA_table

