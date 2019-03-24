# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:05:09 2019

@author: Zhaobin
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('mpg.csv')


def func_color(x):
    if x == "f":
        return 'r'
    elif x == "4":
        return "b"
    else:
        return "k"
df['color'] = df['drv'].apply(func_color)

# plot the figure
plt.figure()
plt.scatter(df['displ'].tolist(), df['hwy'].tolist(), 
            color = df['color'].tolist())

# plot with transparency
plt.figure()
plt.scatter(df['displ'].tolist(), df['hwy'].tolist(), 
            color = df['color'].tolist(),
            alpha = 0.3)

# plot with jittering and transparency
sns.regplot(x='displ',
            y='hwy',
            data=df,
            fit_reg=False,  # do not fit a regression line
            x_jitter=0.1,  # could also dynamically set this with range of data
            y_jitter=0.1,
            scatter_kws={'alpha': 0.3, 'color': df['color'].tolist()}
            )  # set transparency to 50%

# plot with transparency and too much jitting
sns.regplot(x='displ',
            y='hwy',
            data=df,
            fit_reg=False,  # do not fit a regression line
            x_jitter=0.5,  # could also dynamically set this with range of data
            y_jitter=0.5,
            scatter_kws={'alpha': 0.3, 'color': df['color'].tolist()}
            )  # set transparency to 50%