#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:41:28 2018

@author: Samuel_Clarin
"""

##import anova and other programs

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

from plotnine import *

#importing data

sugar=pd.read_csv("sugar.csv", header=0, sep=",")
antibiotics=pd.read_csv("antibiotics.csv", header=0, sep=",")

#graphing

ggplot(antibiotics, aes(x="trt",y="growth"))+geom_jitter()