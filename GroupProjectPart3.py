# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:04:55 2018

@author: Alicia
"""
#Questions:
#How to make anova function definition - equation
#How to make anova datasets where we have groups for each level
#How to make 10 different random datasets
#Finding p-values

import numpy
import pandas as pd
import scipy
from scipy import stats
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
df.groupby(['])
# plot our observations
ggplot(df,aes(x='x',y='y'))+geom_point()+theme_classic()
    
sigma_list[1,2,4,6,8,12,16,24]

def NullMod(p,obs):
    B0=p[0]
    sigma=p[1]
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

def anova2Mod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=
    anova2=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova2
    
def anova4Mod(p,obs):
    B0=p[0]
    B1=p[1]
    B2=p[2]
    B3=p[3]
    sigma=p[4]
    
    expected=
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
    sigma=p[7]
    expected=
    anova8=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return anova8
    
for i in range(0,10): 
    for n in sigma_list:
        NullGuess=numpy.array([10,n])
        fitNull_'n'=minimize(NullMod,NullGuess,method="Nelder-Mead",args=df)

for n in sigma_list:
    RegressionGuess=numpy.array([10,0.4,n])
    fitRegression_n=minimize(RegMod,RegressionGuess,method="Nelder-Mead",args=df)

for n in sigma_list:
    anova2Guess=numpy.array([10,0.4,n])
    fitanova2_n=minimize(anova2Mod,anova2Guess,method="Nelder-Mead",args=df)

for n in sigma_list:
    anova4Guess=numpy.array([10,0.4,n])
    fitanova4_n=minimize(anova4Mod,anova4Guess,method="Nelder-Mead",args=df)

for n in sigma_list:
    anova8Guess=numpy.array([10,0.4,n])
    fitanova8_n=minimize(anova8Mod,anova8Guess,method="Nelder-Mead",args=df)

for i in range(0,10):

    for n in sigma_list:
        teststat=2*(fitNull_n_i.fun-fitRegression_n.fun)
        data=len(fitRegression_n.x)-len(fitNull_n.x)
        pval_n=1-chi2.cdf(teststat,data)
    
# Fit the model
#model = ols("y ~ x", df).fit()


#running ANOVA

#Fit the model
model=ols('', data=df).fit()
model.summary()
print(model.summary())
#Perform ANOVA on linear model
ANOVA_results=sm.stats.anova_lm(model, typ=2)
print('\nANOVA results')
print(ANOVA_results)


F, p = stats.f_oneway(d_df[], d_df[])



#B[0]=10 #y-int
#B[1]=0.4 #slope
#two level ANOVA w/ 12 times each level
#sigma=1,2,4,6,8,12,16,24

#four level ANOVA w/ 6 times each level

#eight level ANOVA w/ 3 times each level



#either make 5 different for loops or put loop as one of the arguments called in definition function
#need 5 diff def functions (null, regression, 2/4/8 level ANOVA)
