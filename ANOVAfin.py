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
import statsmodels.api as sm
from statsmodels.formula.api import ols
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm
#importing data

anti=pd.read_csv("antibiotics.csv", header=0, sep=",")

#visualizing data

ggplot(antibiotics, aes(x="trt",y="growth"))+geom_boxplot()

#running ANOVA

anti.head()
antifix=pd.DataFrame({"x1":[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]})
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
    expected=B0+B1*obs.x+B2*obs.x+B3*obs.x
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll

### estimate parameters by minimizing the negative log likelihood
initialGuess=np.array([1,1])
initialGuess1=np.array([1,1,1,1,1])
fitNull=minimize(NullMod,initialGuess,method="Nelder-Mead",options={'disp': True},args=df)
fitAnova=minimize(ANOVA,initialGuess1,method="Nelder-Mead",options={'disp': True},args=df)
# fit is a variable that contains an OptimizeResult object
# attribute 'x' is a list of the most likely parameter values
print(fitAnova.x)

from scipy import stats
teststat=2*(fitNull.fun-fitAnova.fun)
df2=len(fitAnova.x)-len(fitNull.x)
p=1-stats.chi2.cdf(teststat,df2)

print (teststat)
print (df2)
print (p)



import pandas as pd
datafile = "PlantGrowth.csv"
data = pd.read_csv(datafile)
 
#Create a boxplot
antibiotics.boxplot('growth', by='trt')
 
ctrl = antibiotics['growth'][antibiotics.group == 'trt']
 
grps = pd.unique(antibiotics.growth.values)
d_data = {grp:antibiotics['trt'][antibiotics.growth == grp] for grp in grps}
 
k = len(pd.unique(antibiotics.growth))  # number of conditions
N = len(antibiotics.values)  # conditions times participants
n = antibiotics.groupby('trt').size()[0] #Participants in each condition
DFbetween = k - 1
DFwithin = N - k
DFtotal = N - 1
SSbetween = (sum(antibiotics.groupby('trt').sum()['growth']**2)/n) \
    - (antibiotics['growth'].sum()**2)/N

sum_y_squared = sum([value**2 for value in antibiotics['growth'].values])
SSwithin = sum_y_squared - sum(antibiotics.groupby('trt').sum()['growth']**2)/n

SStotal = sum_y_squared - (antibiotics['growth'].sum()**2)/N

MSbetween = SSbetween/DFbetween

MSwithin = SSwithin/DFwithin

F = MSbetween/MSwithin

p = stats.f.sf(F, DFbetween, DFwithin)
p



