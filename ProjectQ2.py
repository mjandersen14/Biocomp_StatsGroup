#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:50:28 2018

@author: marissaandersen
"""
#NUMBER 2
#import things 
import numpy 
import pandas as pd
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm

#Import sugar.txt
sugar=pd.read_csv('sugar.csv', header=0, sep="," )

#create graph of data 
ggplot(sugar,aes(x="sugar", y="growth"))+geom_point()+theme_classic()

#create a liklihood test 
def regression(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.sugar
    reg=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return reg 

initialGuess=numpy.array([1,1,1])
fit=minimize(regression,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)

def null(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return nll 

initialGuess=numpy.array([1,1])
fitnull=minimize(null,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)

print (fit,fitnull)
# fit is a variable that contains an OptimizeResult object
# attribute 'x' is a list of the most likely parameter values


from scipy import stats 

teststat=2*(fitnull.fun-fit.fun)
df=len(fit.x)-len(fitnull.x) #can't be 0 so what is wrong? 
pval=1-stats.chi2.cdf(teststat,df)  
print (pval)




#find a p-value 
#sentence about plot do we need a regression line on our plot? 
#do we care about the effect of sugar on growth ... answer 













































