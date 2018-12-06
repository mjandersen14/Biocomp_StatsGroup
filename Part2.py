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

#make a function for regression and null 
def regression(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.sugar
    reg=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return reg 

def null(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return nll 

#optimize regression and null 
initialGuess=numpy.array([1,1,1])
fit=minimize(regression,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)

initialGuess=numpy.array([1,1])
fitnull=minimize(null,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)

print (fit,fitnull)

#find p-value
from scipy import stats 

teststat=2*(fitnull.fun-fit.fun)
df=len(fit.x)-len(fitnull.x) 
pval=1-stats.chi2.cdf(teststat,df)  
print (pval)
 
#The graph depicting amount of sugar to growth sugests that there is a possitive correlation between the amount of sugar E.coli recieve and how much they grow. 
#This hypothesis was tested using a regression analysis getting a p-value of 2.6389e-10. 
#The p-value is very low so we are able to reject the null hypothesis that sugar does't have an effect on growth of E.coli. 
 













































