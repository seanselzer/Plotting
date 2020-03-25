#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:32:57 2020

@author: seanselzer
"""

from plot_stencil import my_plotter

rainbow_df = pd.read_excel('/Users/seanselzer/Documents/Education/Oxford/DPhil/Manuscripts/FRidge_Radium_Paper/FRidge_Data_Analysis/Rainbow_Analysis.xlsx', sheet_name = 'Main')
tag_df = pd.read_excel('/Users/seanselzer/Documents/Education/Oxford/DPhil/Manuscripts/FRidge_Radium_Paper/FRidge_Data_Analysis/TAG_Analysis.xlsx', sheet_name = 'Main')

"""
Rainbow
-------
"""

f, ([ax1, ax2], [ax3, ax4]) = plt.subplots(2, 2, sharey = 'row', sharex = 'col', figsize = [4.8*1.3, 6.4*1.3], dpi = 175)

ax1.set(xlabel='', ylabel='Depth (m)',
       title='')
ax2.set(xlabel='', ylabel='',
       title='')

deployment_set = set(rainbow_df.Deployment)
deployment_list = list(deployment_set)
deployment_list.sort()

for deployment in deployment_list:
    
    my_plotter(ax1, 
               rainbow_df[rainbow_df.Deployment == deployment].xs224, 
               rainbow_df[rainbow_df.Deployment == deployment].Depth, 
               {'linestyle': '-',
                                  'marker': 'o',
                                  'markeredgecolor' : 'black',
                                  'label':deployment},
               y_lim_max = rainbow_df.Depth.max()*1.05,
               y_lim_min = rainbow_df.Depth.min()*1.05)
               
    my_plotter(ax2, 
               rainbow_df[rainbow_df.Deployment == deployment].xs223, 
               rainbow_df[rainbow_df.Deployment == deployment].Depth, 
               {'linestyle': '-',
                                  'marker': 'o',
                                  'markeredgecolor' : 'black',
                                  'label':deployment},
                y_lim_max = rainbow_df.Depth.max()*1.05,
                y_lim_min = rainbow_df.Depth.min()*0.95)
    ax2.legend()

#plt.savefig('rainbow_results_fig_223224.png')


"""
TAG
---
"""

ax3.set(xlabel='Radium-224 Excess (dpm/1000 L)', ylabel='Depth (m)',
       title='')
ax4.set(xlabel='Radium-223 Excess (dpm/1000 L)', ylabel='',
       title='')

deployment_set = set(tag_df.Deployment)
deployment_list = list(deployment_set)
deployment_list.sort()


for deployment in deployment_list:
    
    my_plotter(ax3, 
               tag_df[tag_df.Deployment == deployment].xs224, 
               tag_df[tag_df.Deployment == deployment].Depth, 
               {'linestyle': '-',
                                  'marker': 'o',
                                  'markeredgecolor' : 'black',
                                  'label':deployment},
               y_lim_max = tag_df.Depth.max()*1.05,
               y_lim_min = tag_df.Depth.min()*1.05)
               
    my_plotter(ax4, 
               tag_df[tag_df.Deployment == deployment].xs223, 
               tag_df[tag_df.Deployment == deployment].Depth, 
               {'linestyle': '-',
                                  'marker': 'o',
                                  'markeredgecolor' : 'black',
                                  'label':deployment},
                y_lim_max = tag_df.Depth.max()*1.05,
                y_lim_min = tag_df.Depth.min()*0.95)
    ax4.legend()
    
plt.savefig('all_results_fig_223224.png')   
#
#f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, dpi = 125)
#
#ax1.set(xlabel='xs224', ylabel='Depth (m)',
#       title='')
#ax2.set(xlabel='xs223', ylabel='',
#       title='')
#
#
#my_plotter(ax1, tag_df.xs224, tag_df.Depth, {'linestyle': '',
#                              'marker': 'o',
#                              'markerfacecolor' : 'red',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'})
#
#
#my_plotter(ax1, tag_df.xs224_scav, tag_df.Depth, {'linestyle': '',
#                              'marker': 'o',
#                              'markerfacecolor' : 'teal',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'})
#
#my_plotter(ax2, tag_df.xs223, tag_df.Depth, {'linestyle': '',
#                              'marker': 'o',
#                              'markerfacecolor' : 'red',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'})
#
#
#my_plotter(ax2, tag_df.xs223_scav, tag_df.Depth, {'linestyle': '',
#                              'marker': 'o',
#                              'markerfacecolor' : 'teal',
#                              'markeredgecolor' : 'black',
#                              'label':'Data1'})