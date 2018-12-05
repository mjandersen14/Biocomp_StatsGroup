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
from scipy import stats 

#Import sugar.txt
sugar=pd.read_csv('sugar.csv', header=0, sep="," )

#create graph of data 
ggplot(sugar,aes(x="sugar", y="growth"))+geom_point()+theme_classic()

#regression  
def regression(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.sugar
    reg=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return reg 

initialGuess=numpy.array([1,1,1])
fit=minimize(regression,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)

#null 
def null(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return nll 

initialGuess=numpy.array([1,1])
fitnull=minimize(null,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)

print (fit,fitnull)

#find p-value
from scipy import stats 

teststat=2*(fitnull.fun-fit.fun)
df=len(fit.x)-len(fitnull.x) 
pval=1-stats.chi2.cdf(teststat,df)  
print (pval)

print ()
#sentence about plot do we need a regression line on our plot? 
#because our p-value is low we can reject the null hypothesis. This tells us 
#we do care about the effect of sugar on growth













































