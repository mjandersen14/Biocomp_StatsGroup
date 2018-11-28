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
def nllike(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.sugar
    nll=-1*norm(expected,sigma).logpdf(obs.growth).sum()
    return nll
### estimate parameters by minimizing the negative log likelihood
initialGuess=numpy.array([1,1,1])
fit=minimize(nllike,initialGuess,method="Nelder-Mead",options={'disp': True},args=sugar)
# fit is a variable that contains an OptimizeResult object
# attribute 'x' is a list of the most likely parameter values
print(fit)
















































