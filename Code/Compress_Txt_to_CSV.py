# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:37:58 2020

@author: dakersey
"""
import os
import pandas as pd
import functools

data_path = '/Users/dakersey/Documents/NLS/GIthub/NLP-Use-of-Force-master/Data/Cleaned_Text/'

def bind_rows(dfs, ignore_index=True):
    return functools.reduce(lambda t,b: pd.concat([t,b], ignore_index=ignore_index), dfs)


header_list = ['Policy']

files = []
for i in os.listdir(data_path):
    txt = os.path.join(data_path, str(i))
    city = i.split('_')[0]
    if 'Extract_processed' in txt:
        f = pd.read_csv(txt, names=header_list)
        f['City'] = city
        f = f[['City','Policy']]
        files.append(f)

df = bind_rows(files)

