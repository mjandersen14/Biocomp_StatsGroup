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

#define function for 2-way ANOVA
def anova2Mod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.x1
    anova2=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova2
    
#define function for 4-way ANOVA
def anova4Mod(p,obs):
    B0=p[0]
    B1=p[1]
    B2=p[2]
    B3=p[3]
    sigma=p[4]
    expected=B0+B1*obs.x1+B2*obs.x2+B3*obs.x3
    anova4=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova4
    
#define function for 8-way ANOVA
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
    
#necessary dataframes
sigma_list=[1,2,4,6,8,12,16,24]
d=0
s=0
summary=numpy.zeros(shape=(8,4))
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

#where the calculations happen
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
       
       #add df to dummyframe
       A2f=A2.join(df)
       #Split data into 2 groups
       sorted=A2f.sort_values(by=['x'])
       Anova2G1=sorted.head(12)
       Anova2G2=sorted.tail(12)
       
       #get stats on anova 2 level
       anova2Guess=numpy.array([10,0.4,1])
       fitanova2=minimize(anova2Mod,anova2Guess,method="Nelder-Mead",args=A2f)
       
       #compare anova 2 level and null to get p-value
       teststat=2*(fitNull.fun-fitanova2.fun)
       data=len(fitanova2.x)-len(fitNull.x)
       pval2=1-stats.chi2.cdf(teststat,data)
       
       #add p-vals to list 
       a2Pvals.append(pval2)
       
       #split data into 4 groups
       A4f=A4.join(df) 
       
       #get stats on anova 4 level
       anova4Guess=numpy.array([10,0.4,10,10,1])
       fitanova4=minimize(anova4Mod,anova4Guess,method="Nelder-Mead",args=A4f)
       
       #compare anova 4 level and null to get p-value
       teststat=2*(fitNull.fun-fitanova4.fun)
       data=len(fitanova4.x)-len(fitNull.x)
       pval4=1-stats.chi2.cdf(teststat,data)
       
       #add p-vals to list 
       a4Pvals.append(pval4)
       
       #add df to dummyframe
       A8f=A8.join(df)
       
       #get stats on anova 8 level
       anova8Guess=numpy.array([10,0.4,10,10,10,10,10,10,1])
       fitanova8=minimize(anova8Mod,anova8Guess,method="Nelder-Mead",args=A8f)
       
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
columns=['Regression Pvals','2-way ANOVA Pvals','4-way ANOVA Pvals','8-way ANOVA Pvals']
sigma=['1','2','4','6','8','12','16','24']
finalsum=pd.DataFrame(data=summary,
                  index=sigma,
                  columns=columns)
print(finalsum)



























