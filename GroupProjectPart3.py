# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:04:55 2018

@author: Alicia
"""

import numpy as np
import pandas as pd
import statsmodels
from statsmodels.formula.api import ols
#Analysis of Variance (ANOVA) for linear models
from statsmodels.stats.anova import anova_lm
from plotnine import *


#Create random dataset with 24 observations of y


sigma_list[1,2,4,6,8,12,16,24]

def RegMod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]

    expected=B0+B1*obs.x
    nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll

for n in sigma_list:
    do
    RegressionGuess$n=numpy.array([10,0.4,"$n"])
fitRegression=minimize(RegMod,RegressionGuess,method="Nelder-Mead",args=df)

teststat=2*(Regression.fun-fitQuadratic.fun)
data=len(fitQuadratic.x)-len(fitLinear.x)
1-chi2.cdf(teststat,data)


x = np.linspace(-5, 5, 20)

# To get reproducable values, provide a seed value
np.random.seed(1)

y = -5 + 3*x + 4 * np.random.normal(size=x.shape)

# Plot the data
plt.figure(figsize=(5, 4))
plt.plot(x, y, 'o')

B[0]=10 #y-int
B[1]=0.4 #slope
#two level ANOVA w/ 12 times each level
#sigma=1,2,4,6,8,12,16,24

#four level ANOVA w/ 6 times each level

#eight level ANOVA w/ 3 times each level