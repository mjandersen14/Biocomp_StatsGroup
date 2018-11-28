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




#number 1 
anti=pd.read_csv('antibiotics.csv', header=0, sep='\t')
ggplot(anti,aes(x="trt", y="growth"))+geom_point()+theme_classic()





























### Simulating Data 
import numpy
import pandas
from scipy.optimize import minimize
from scipy.stats import norm
from plotnine import *
### Simulating data (do this for the last part) 
# creating a uniformly distributed set of values for an independent variable x
# and values for a variable y that is linearly dependent on x
N=24
x=numpy.random.uniform(0,20,size=N)
#3 is the slope of the line and 5 is the y intercept 
y=3*x+5
# add some "noise" to y and put the variables in a dataframe, *3 will determin how tight of a fit we will have
#basicly we are taking the y values that would make a perfect fit and added a random number to it then multiplied that by 3 to get more varrience  
y=y+numpy.random.randn(N)*3 
df=pandas.DataFrame({'x':x,'y':y})
# plot our observations
ggplot(df,aes(x='x',y='y'))+geom_point()+theme_classic()




#NOV 7 LECTURE 
### Custom likelihood function
#defining a costom function 
def nllike(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.x
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll
### estimate parameters by minimizing the negative log likelihood
initialGuess=numpy.array([1,1,1])
fit=minimize(nllike,initialGuess,method="Nelder-Mead",options={'disp': True},args=df)
# fit is a variable that contains an OptimizeResult object
# attribute 'x' is a list of the most likely parameter values
print(fit.x)

###CHALLENGE 



























