# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:30:36 2019

@author: Zhaobin
"""

import pandas as pd
import re

# read the data
PATTERN = re.compile(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)')
with open('input.txt', encoding = 'latin-1', mode='r') as f:
    # pandas is used here
    df = pd.DataFrame(PATTERN.split(l.rstrip('\n').replace("\x00","").replace("NA",'0').replace("--",'0')) for l in f)

# delete the none
mask = pd.isnull(df[1])
df = df.loc[~mask,:]

# reset the index and the colname
df = df.set_index(df[0])
df = df.iloc[:,1:32]

headers = df.iloc[0]
df  = pd.DataFrame(df.values[1:], columns=headers)

df['2010'] = df['2010'].apply(lambda x : 0 if x == '"0"' else x )
df['2010'] = df['2010'].astype(float)


def test_read_file():
    assert df.shape[1] == 31
    assert df.shape[0] == 225

def test_population():
    assert round(sum(df['2010'].values)) == 7065
