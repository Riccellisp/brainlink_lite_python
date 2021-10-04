#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:42:15 2021

@author: riccelli
"""
import pandas as pd
import os
from pylive import live_plotter
import numpy as np

def realtime_plot(signal,title):
    size = len(signal) + 1
    x_vec = np.linspace(0,100,size+1)[0:-1]
    line1 = []
    while True:
        signal[-1] = signal[0]
        line1 = live_plotter(x_vec,signal,line1,identifier=title)
        signal = np.append(signal[1:],0.0)

os.chdir('../../')
records = pd.read_csv('code/jupyter/brainlink_lite 100 seconds.csv')

for col in records.columns:
    reg = records[col]
    realtime_plot(reg,col)
    
# import pandas as pd
# import os
# from pylive import live_plotter
# import numpy as np

# os.chdir('../../')
# records = pd.read_csv('code/jupyter/brainlink_lite 100 seconds.csv')

# for col in records.columns:
#     reg = records[col]
#     size = 95
#     x_vec = np.linspace(0,100,size+1)[0:-1]
#     y_vec = reg
#     line1 = []
#     while True:
#         y_vec[-1] = y_vec[0]
#         line1 = live_plotter(x_vec,y_vec,line1)
#         y_vec = np.append(y_vec[1:],0.0)