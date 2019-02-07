# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:20:39 2019

@author: Zhaobin
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.ticker
from matplotlib.ticker import FuncFormatter

df_population = pd.read_csv("Puerto Rico Commonwealth Population Totals and Components of Change 2010-2018.csv", index_col = 0)
df_phd = pd.read_excel("statistic_id185167_doctoral-degrees-earned-in-the-united-states-by-gender-1950-2028.xlsx")

df_phd['sum'] = df_phd.Male + df_phd.Female

df_phd = df_phd.reset_index()

# the polation from 2010 to 2018
list_population = df_population.iloc[0,0:9]

# the phd earned from 2010 to 2018
list_phd = df_phd.iloc[43:52,2]

# the year list
list_year = [x for x in range(2010,2019)]

def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x*1e-6)
mil_formatter = FuncFormatter(millions)
# plot the figure
nticks = 5
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(list_year, list_population, "ro-")
ax2.plot(list_year, list_phd, "bD-")

ax1.set_xlabel('year')
ax1.set_ylabel('Puerto Rico Commonwealth Population Totals of U.S.')
#ax1.tick_params(labeltop=True)
ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
ax1.yaxis.grid(True)
ax2.set_ylabel('Doctoral Degree awarded in the U.S.')
ax1.yaxis.set_major_formatter(mil_formatter)
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter("%d degrees"))
ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))

plt.title('Puerto Rico Commonwealth Population v.s. Doctoral Degree awarded')



