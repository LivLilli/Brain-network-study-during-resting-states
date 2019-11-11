#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:15:33 2019

@author: livialilli
"""

from PDC import PDC

if __name__=="__main__":
    ### TASK 1.1
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # density 20%
    density1 = 0.20
    alpha_freq = (8, 13)
    # initialize PDC class for file1
    pdc1 = PDC(file1, alpha_freq)
    # heatmap file 1
    pdc1.binary_heatmap(density1)
    # initialize PDC class for file2
    pdc2 = PDC(file2, alpha_freq)
    # heatmap file 2
    pdc2.binary_heatmap(density1)
