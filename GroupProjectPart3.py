# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:04:55 2018

@author: Alicia
"""

import numpy
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
#Analysis of Variance (ANOVA) for linear models
from statsmodels.stats.anova import anova_lm
from plotnine import *


#Create random dataset with 24 observations of y
#random data set 
N=24
x=numpy.random.uniform(0,50,size=N)
#0.4 is the slope of the line and 10 is the y intercept 
y=0.4*x+10
# add some "noise" to y and put the variables in a dataframe, *3 will determin how tight of a fit we will have
#basically we are taking the y values that would make a perfect fit and added a random number to it then multiplied that by 3 to get more variance  
y=y+numpy.random.randn(N)*3
# Convert the data into a Pandas DataFrame to use the formulas framework in statsmodels
df=pd.DataFrame({'x':x,'y':y})
# plot our observations
ggplot(df,aes(x='x',y='y'))+geom_point()+theme_classic()
    

sigma_list[1,2,4,6,8,12,16,24]

def NullMod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]

    expected=B0
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll

def RegMod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]

    expected=B0+B1*obs.x
    Reg=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return Reg

for n in range(0,10):
    
    
for n in sigma_list:
    do
    RegressionGuess=numpy.array([10,0.4,n])
fitRegression=minimize(RegMod,RegressionGuess,method="Nelder-Mead",args=df)
    return fitRegression

def ANOVAmod(p,obs):


# Fit the model
#model = ols("y ~ x", df).fit()


#running ANOVA

#Fit the model
model=ols('', data=#insert dataframe here).fit()
model.summary()
print(model.summary())
#Perform ANOVA on linear model
ANOVA_results=sm.stats.anova_lm(model, typ=2)
print('\nANOVA results')
print(ANOVA_results)


#B[0]=10 #y-int
#B[1]=0.4 #slope
#two level ANOVA w/ 12 times each level
#sigma=1,2,4,6,8,12,16,24

#four level ANOVA w/ 6 times each level

#eight level ANOVA w/ 3 times each level



#either make 5 different for loops or put loop as one of the arguments called in definition function
#need 5 diff def functions (null, regression, 2/4/8 level ANOVA)
