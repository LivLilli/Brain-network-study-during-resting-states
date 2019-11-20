#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:33:03 2019

@author: livialilli
"""
from task_2_123 import task_2_1



'''
Compare the networks obtained with the analysis 1.6 in terms of graph indices.
'''


if __name__=="__main__":
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # density 20%
    density1 = 0.20
    # theta rythm
    theta_range = (4,7)
    
    
    task_2_1(file1, density1, theta_range)
    task_2_1(file2, density1, theta_range)
    
    
