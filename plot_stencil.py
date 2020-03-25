#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:09:49 2020

@author: seanselzer
"""

import matplotlib.pyplot as plt
import numpy as np

def my_plotter(ax, data1, data2, param_dict, y_lim_max, y_lim_min) :
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    ax.set_ylim(y_lim_max, y_lim_min)
    return out

# which you would then use as:
#
#data1, data2, data3, data4 = np.random.randn(4, 100)
#fig, ax = plt.subplots(1, 1)
#my_plotter(ax, data1, data2, {'linestyle': '',
#                              'marker': 'o',
#                              'markerfacecolor' : 'teal',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'}, 3,-3)
