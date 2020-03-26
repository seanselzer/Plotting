#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:35:53 2020

@author: seanselzer
"""

from plot_stencil import my_plotter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#IDP2017 = pd.read_excel('/Users/seanselzer/Documents/Education/Oxford/DPhil/Manuscripts/FRidge_Radium_Paper/FRidge_Data_Analysis/GEOTRACES_IDP2017_v2/discrete_sample_data/excel/GEOTRACES_IDP2017_v2_Discrete_Sample_Data.xlsx')
GA03 = IDP2017[IDP2017.Cruise == 'GA03']
GA03 = GA03[GA03['PRESSURE [dbar]']>1000]
GA03.dropna()
Longitude = GA03['Longitude [degrees_east]']
ra223 = GA03['Ra_223_D_CONC_PUMP [mBq/kg]']*60
ra224 = GA03['Ra_224_D_CONC_PUMP [mBq/kg]']*60
fig, ax = plt.subplots(1, 1)

my_plotter(ax, Longitude, ra223/ra224, {'linestyle': '',
                              'marker': 'o',
                              'markerfacecolor' : 'grey',
                              'markeredgecolor' : 'black',
                              'label':'Data1'}, 0, 10, True)


#my_plotter(ax, Longitude, ra223, {'linestyle': '',
#                              'marker': 'x',
#                              'markerfacecolor' : 'red',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'}, 0, 10, True)
#
#my_plotter(ax, Longitude, ra224, {'linestyle': '',
#                              'marker': 'x',
#                              'markerfacecolor' : 'teal',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'}, 0, 10, True)
GA03.sort_values(by=['Longitude [degrees_east]'])
data1 = GA03['Longitude [degrees_east]']
data2 = GA03['Bot. Depth [m]']

fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'linestyle': '',
                              'marker': 'o',
                              'markerfacecolor' : 'teal',
                              'markeredgecolor' : 'black',
                              'label':'Data1'}, 7000, 0, True)

