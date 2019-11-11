#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:17:06 2019

@author: livialilli
"""
from PDC import PDC

### TASK 1.6
# Perform task 1.1 considering a second frequency value 
# belonging to a different EEG rhythm with respect to the first choice


if __name__=="__main__":
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # density 20%
    density1 = 0.20
    # theta rythm
    theta_range = (4, 7)
    
    pdc3 = PDC(file1, theta_range)
    pdc4 = PDC(file2, theta_range)
    
    pdc3.binary_heatmap(density1)
    pdc4.binary_heatmap(density1)