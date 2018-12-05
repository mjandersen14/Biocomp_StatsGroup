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

#running ANOVA
N=16
y=.4*x+5
# add some "noise" to y and put the variables in a dataframe
y=y+np.random.randn(N)
antifixNull=pd.DataFrame({"x":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          "y": anti.growth})
antifixA4=pd.DataFrame({"x1":[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                      "x2":[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0], 
                      "x3":[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
                      "y": anti.growth})
A2=pd.DataFrame({"x1":[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]})
A4=pd.DataFrame({"x1":[0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                      "x2":[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0], 
                      "x3":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]})
A8=pd.DataFrame({"x1":[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      "x2":[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                      "x3":[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                      "x4":[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                      "x5":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                      "x6":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
                      "x7":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]})

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

### estimate parameters by minimizing the negative log likelihood
initialGuess=np.array([1,1])
initialGuess1=np.array([1,1,1,1,1])
fitNull=minimize(NullMod,initialGuess,method="Nelder-Mead",options={'disp': True},args=antifixNull)
fitAnova=minimize(ANOVA,initialGuess1,method="Nelder-Mead",options={'disp': True},args=antifixA4)
# fit is a variable that contains an OptimizeResult object
# attribute 'x' is a list of the most likely parameter values
print(fitAnova.x)


teststat=2*(fitNull.fun-fitAnova.fun)
df2=len(fitAnova.x)-len(fitNull.x)
p=1-stats.chi2.cdf(teststat,df2)

print (teststat)
print (df2)
print (p)




