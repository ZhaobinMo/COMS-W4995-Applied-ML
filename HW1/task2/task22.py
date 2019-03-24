# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:28:28 2019

@author: Zhaobin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
target =data.target
target_names = data.target_names
feature_names = data.feature_names
data = data.data

def func_color(x):
    if x == 0:
        return 'r'
    elif x == 1:
        return 'b'
    else:
        return 'g'
    
color_list = [func_color(x) for x in target]
# plot
for i in range(4):
    for j in range(4):
        plt.subplot(4,4,4*i + j+1)
        if i == j:
            plt.hist(data[:,i])
        else:
            plt.scatter(data[:,i], data[:,j], color = color_list)
        if j == 0:
            plt.ylabel(feature_names[i])
        if i == 3:
            plt.xlabel(feature_names[j])

#### lack legend and there is gap between the subfigure