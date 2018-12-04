#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:34:13 2018

@author: marissaandersen
"""

import numpy
import pandas as pd
from scipy import stats
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm
from scipy import stats 



#define function for regression 
def regression(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.x
    reg=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return reg 

#define function for null
def null(p,obs):
    B0=p[0]
    sigma=p[1]
    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll

def anova2Mod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.x1
    anova2=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova2
    
def anova4Mod(p,obs):
    B0=p[0]
    B1=p[1]
    B2=p[2]
    B3=p[3]
    sigma=p[4]
    expected=B0+B1*obs.x1+B2*obs.x2+B3*obs.x3
    anova4=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova4
    
def anova8Mod(p,obs):
    B0=p[0]
    B1=p[1]
    B2=p[2]
    B3=p[3]
    B4=p[4]
    B5=p[5]
    B6=p[6]
    B7=p[7]
    sigma=p[8]
    expected=B0+B1*obs.x1+B2*obs.x2+B3*obs.x3+B4*obs.x4+B5*obs.x5+B6*obs.x6+B7*obs.x7
    anova8=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova8
    
def mean(data):
     return sum(data) / len(data)
    


sigma_list=[1,2,4,6,8,12,16,24]
d=0
summary=numpy.zeros(shape=(8,4))

for s in range (0,len(sigma_list)):
   rPvals=[]
   a2Pvals=[]
   a4Pvals=[]
   a8Pvals=[]
   for d in range (0,10):
       #creates a random data set
       N=24
       x=numpy.random.uniform(0,50,size=N)
       y=0.4*x+10
       y=y+numpy.random.randn(N)*sigma_list[s]
       df=pd.DataFrame({'x':x,'y':y})  
       #d=d+1
       
       #get stats on regression 
       RegressionGuess=numpy.array([10,0.4,1])
       fitRegression=minimize(regression,RegressionGuess,method="Nelder-Mead",args=df)
       
       #get stats on null
       NullGuess=numpy.array([10,1])
       fitNull=minimize(null,NullGuess,method="Nelder-Mead",args=df)
       
       #Compare regression and null to get p-value
       teststat=2*(fitNull.fun-fitRegression.fun)
       data=len(fitRegression.x)-len(fitNull.x)
       regressionpval=1-stats.chi2.cdf(teststat,data)
       
       #add p-vals to list 
       rPvals.append(regressionpval)
       
       
       #Split data into 2 groups
       sorted=df.sort_values(by=['x'])
       Anova2G1=sorted.head(12)
       Anova2G2=sorted.tail(12)
       #get into a format we can use 
       #get rid of the x axis variables
       
       #get stats on anova 2 level
       anova2Guess=numpy.array([10,0.4,1])
       fitanova2=minimize(anova2Mod,anova2Guess,method="Nelder-Mead",args=df)
       
       #compare anova 2 level and null to get p-value
       teststat=2*(fitNull.fun-fitanova2.fun)
       data=len(fitanova2.x)-len(fitNull.x)
       pval2=1-stats.chi2.cdf(teststat,data)
       
       #add p-vals to list 
       a2Pvals.append(pval2l)
       
       
       #split data into 6 groups
       Anova6G6=sorted.tail(4)
       sorted=sorted[:-4]
       Anova6G5=sorted.tail(4)
       sorted=sorted[:-4]
       Anova6G4=sorted.tail(4)
       sorted=sorted[:-4]
       Anova6G3=sorted.tail(4)
       sorted=sorted[:-4]
       Anova6G2=sorted.tail(4)
       sorted=sorted[:-4]
       Anova6G1=sorted.tail(4)
       #now get in a format we can use  
       
       #get stats on anova 4 level
       anova4Guess=numpy.array([10,0.4,10,10,1])
       fitanova4=minimize(anova4Mod,anova4Guess,method="Nelder-Mead",args=df)
       
       #compare anova 4 level and null to get p-value
       teststat=2*(fitNull.fun-fitanova4.fun)
       data=len(fitanova4.x)-len(fitNull.x)
       pval4=1-stats.chi2.cdf(teststat,data)
       
       #add p-vals to list 
       a4Pvals.append(pval4)
       
       
       #split data into 8 groups 
       sorted=df.sort_values(by=['x'])
       Anova8G8=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G7=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G6=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G5=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G4=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G3=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G2=sorted.tail(3)
       sorted=sorted[:-3]
       Anova8G1=sorted.tail(3)
       #get into a format we can use
       obs=the DataFrame
       
       #get stats on anova 8 level
       anova8Guess=numpy.array([10,0.4,10,10,10,10,10,10,1])
       fitanova8=minimize(anova8Mod,anova8Guess,method="Nelder-Mead",args=df)
       
       #compare anova 8 level and null to get p-value
       teststat=2*(fitNull.fun-fitanova8.fun)
       data=len(fitanova8.x)-len(fitNull.x)
       pval8=1-stats.chi2.cdf(teststat,data)
       
       #add p-vals to list 
       a8Pvals.append(pval8)
       
   #find the mean of sigmas on 10 runthoughs in the outside for loop 
   summary [s,0]=mean(rPvals)
   summary [s,1]=mean(a2Pvals) 
   summary [s,2]=mean(a4Pvals)
   summary [s,3]=mean(a8Pvals)
print (summary)

#turn summary into dataframe 

#mean of the p-vals at all sigmas? 
#what do they tell us? 



























