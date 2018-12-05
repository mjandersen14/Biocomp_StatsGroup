#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:41:28 2018

@author: Samuel_Clarin
"""

##import programs

import pandas as pd
import numpy as np
from scipy import stats
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm
from scipy import stats

#importing data
anti=pd.read_csv("antibiotics.csv", header=0, sep=",")

#visualizing data
ggplot(anti, aes(x="trt",y="growth"))+geom_boxplot()

#dummy-code for data 
antifixNull=pd.DataFrame({"x":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          "y": anti.growth})
antifixA4=pd.DataFrame({"x1":[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                      "x2":[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0], 
                      "x3":[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
                      "y": anti.growth})

#define null and ANOVA functions 
def NullMod(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll

def ANOVA(p,obs):
    B0=p[0]
    B1=p[1]
    B2=p[2]
    B3=p[3]
    sigma=p[4]
    expected=B0+B1*obs.x1+B2*obs.x2+B3*obs.x3
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll

#estimate parameters by minimizing the negative log likelihood
#fit is a variable that contains an OptimizeResult object
#attribute 'x' is a list of the most likely parameter values
initialGuess=np.array([1,1])
initialGuess1=np.array([1,1,1,1,1])
fitNull=minimize(NullMod,initialGuess,method="Nelder-Mead",options={'disp': True},args=antifixNull)
fitAnova=minimize(ANOVA,initialGuess1,method="Nelder-Mead",options={'disp': True},args=antifixA4)

print(fitAnova.x)

#compare the null and 2-way ANOVA to get a p-value 
teststat=2*(fitNull.fun-fitAnova.fun)
df2=len(fitAnova.x)-len(fitNull.x)
p=1-stats.chi2.cdf(teststat,df2)

print (p)

#sentence on p-value and if based off of that we are able to reject the null or not and thus if we caer about sugar on growth 


