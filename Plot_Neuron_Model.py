# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:56:36 2015

@author: vigil
"""
####################### For Plots #############################

from matplotlib import rcParams, rc
rcParams.update({'figure.autolayout': True})
rc('text', usetex=True) 
rcParams['text.latex.preamble'] = ['\\usepackage{siunitx}']

import seaborn
color1 = seaborn.color_palette("Set2", 10)[0]     # Em
color2 = seaborn.color_palette("husl", 8)[0]                # Vm
color3 = seaborn.color_palette("Set2", 10)[9]                # Vt
color4 = seaborn.color_palette("Blues")[5]     # spike

#color1 = seaborn.color_palette("Set2", 10)[0]     # Em
#color2 = seaborn.color_palette("Set2", 10)[1]                # Vm
#color3 = seaborn.color_palette("Set2", 10)[2]                # Vt
#color4 = seaborn.color_palette("Set2", 10)[3]     # spike

FONTSIZE_LABEL = 20  #20
FONTSIZE_MARKER = 20  #16
 

GRIDVALUE = False
MARKERSIZE = 16
LINEWIDTH = 5
##############################################################

from Parameters import *
from MNBC_Neuron_Model import MNBC_Neuron_Model

from numpy import array, zeros
from matplotlib.pyplot import plot, legend, ylim, subplot, title, clf, setp, grid, figure, gca, xlabel, ylabel
import seaborn
seaborn.set_style('whitegrid')

y_axis_points = [0, 1, 2, 3, 4, 5, 6, 7]
threshold_mode = 'dynamic'
num_subplot_rows = 1
num_subplot_cols = 1

index = 1 # subplot, active plot index
#Neuron_behavior_order = ['Tonic spiking', 'Phasic spiking', 'Spike frequency adaptation', 
#				  'Class 1', 'Rebound spike', 'Threshold variability', 'Accomodation', 'Integrator',
#				  'Input bistability', 'Hyperpolarization induced spiking' ]
Neuron_behavior_order = ['Phasic spiking']
#FONTSIZE = 16 

for key in Neuron_behavior_order:  
    [timespan, E_m, V_m, V_t, spike, E_m_pseudo] = MNBC_Neuron_Model(key, threshold_mode)
    time = range(timespan)
    figure()
    
    ax1 = subplot(num_subplot_rows, num_subplot_cols, index)
    ax1.grid(b=GRIDVALUE, linestyle='--')

#    ax1.annotate(r'$Threshold$ $voltage$', xy=(84, 4), xytext=(162, 5), arrowprops=dict(facecolor='black', shrink=0, width=3), fontsize = 18, fontweight = 'bold')
#    ax1.annotate(r'$Membrane$ $voltage$', xy=(49, 1.6), xytext=(96, 0.2), arrowprops=dict(facecolor='black', shrink=0, width=3), fontsize = 18, fontweight = 'bold')
#    ax1.annotate(r'$Spike$', xy=(340, 4), xytext=(418, 5), arrowprops=dict(facecolor='black', shrink=0, width=3), fontsize = 18, fontweight = 'bold')
#    ax1.annotate(r'$Em$', xy=(428, -1), xytext=(506, 0), arrowprops=dict(facecolor='black', shrink=0, width=3), fontsize = 18, fontweight = 'bold')
    
    ax1.set_yticks([-2, -1, 0, 1, 2, 3, 4, 5])
    ax1.set_yticklabels(['$0$', '$5$', '$0$', '$1$', '$2$', '$3$' , '$4$', '$5$'])
    
    for tick in ax1.yaxis.get_major_ticks():
        tick.label1.set_fontsize(FONTSIZE_MARKER)

    plot_values = plot(time, V_t, '-', color=list(color3))    
    setp(plot_values, linewidth=LINEWIDTH)

    plot_values = plot(time, V_m, '-', color=list(color2))    
    setp(plot_values, linewidth=LINEWIDTH)

    plot_values = plot(time, spike, 'o', color=list(color4))    
    setp(plot_values, markersize=MARKERSIZE)
    
    plot_values = plot(time, E_m_pseudo, '-', color=list(color1))    
    setp(plot_values, linewidth=LINEWIDTH)
    
    ax1.grid(b=False)
    ylim([-2.9, 5.9])
    

#        tick.label1.set_fontweight('bold')

	#index += 1
	#title('(j) Hyperpolarization induced spiking', fontweight='bold') 
#    xlabel('Time (us)', fontsize = FONTSIZE_LABEL) # fontweight='bold', 
#    ylabel('Voltage (V)', fontsize = FONTSIZE_LABEL)
	#title(key)

ax_fig = gca()
for tick in ax_fig.xaxis.get_major_ticks():
    tick.label1.set_fontsize(FONTSIZE_MARKER)
#        tick.label1.set_fontweight('bold')

#legend(['Threshold voltage', 'Membrane voltage',  'Spike', 'External update voltage'], prop={'size':FONTSIZE_LEGEND}, loc=1, ncol=2, mode="expand", borderaxespad=0.)   
        
#for tick in ax_fig.yaxis.get_major_ticks():
#    tick.label1.set_fontsize(FONTSIZE_MARKER)