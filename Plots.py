# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:51:22 2016

@author: Administrator
"""

import matplotlib.pyplot as plt


def LineGraph(x,y):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot( x, y, 'r')
    ax.set_title('times per hour')
    ax.set_xlabel('hour')
    ax.set_ylabel('times')
    plt.show()