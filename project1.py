# import libraries
import numpy as np
#import mne
#import pandas as pd
#import os
import connectivipy as cp
import pyedflib
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import networkx as nx
#import matplotlib.pyplot as plt



# reading the edf file 
f = pyedflib.EdfReader('files/S003/S003R01.edf')
#number of channels
k = f.signals_in_file
#number of samples 
N = f.getNSamples()[0]
# selecting a channel (f.e. the last)
channel = 63
# getting Sample Frequency
fs = f.getSampleFrequency(channel)
# annotations array
annotations = f.readAnnotations()
# onset from annotations
onset = annotations[0][0]
# duration from annotations
duration = annotations[1][0]
# description from annotations
description = annotations[2][0]
# creating array of data 
# rows must be channels
# cols must be data points
data = np.zeros((k, N))
for i in np.arange(k):
    data[i, :] = f.readSignal(i)


# MVar model fitting on data
# data is an array of dimension kN (k = number of channels, N = number of data points)
# model order, when default None it estimates order using akaike order criteria.
# mvar fitting algorithm, default Yule-Walker 
# matrix A of coefficient   
A_matrix = cp.mvarmodel.Mvar.fit(data)[0]
# model order p
p = A_matrix.shape[0]
# reflection matrix V 
V_matrix = cp.mvarmodel.Mvar.fit(data)[1]


# computing PDC
# pdc_fun return an array (resolution x k x k)
# resolution = fs/2
pdc = cp.conn.pdc_fun(A_matrix, V_matrix, fs, 80)


# extract just the matrices kxk we need, based on alpha [8,13 HZ]
# so return 6 matrices kxk
freq_selection = pdc[7:13]


# mean among the 6 matrices
# return a kxk matrix 
# each component i,j is the mean among the components i,j of the 6 matrices

# initialize the result matrix
mean_matrix= np.zeros((k,k))
# return freq_selection array collapsed in 1 dimension
flat = freq_selection.flatten()
# for each i, compute the mean among the component of 6 matrices on same positions
# add the mean value to our mean_matrix
for i in range(0,k*k):
    mean = (flat[i]+flat[i+k*k]+flat[i+2*k*k]+flat[i+3*k*k]+flat[i+k*k*4]+flat[i+k*k*5])/(freq_selection.shape[0])
    mean_matrix.flat[i] = mean


# we are not interested in self loops
# then delete the diagonal
matrix_no_diagonal = mean_matrix-np.triu(np.tril(mean_matrix))


# choice of the Thrhesold s.t. 
# the resulting binary connectivity matrices have network density equal to 20%.

# grid
thresholds = np.linspace(0.0, 1.0, 10000)
densities = []
# for each t compute density and add it to a list
for t in thresholds:
    adj_mat = np.zeros((k,k))
    adj_mat[matrix_no_diagonal>=t] = 1
    adj_mat[matrix_no_diagonal<t] = 0
    graph = nx.from_numpy_matrix(adj_mat)
    densities.append(round(nx.density(graph),2))
# convert list in array
densities= np.asarray(densities)
# find index positions of densities = 20%
where = np.where(densities==0.20)
# select the middle index among the found ones
# save the corresponding value of threshold
th = thresholds[where[0][len(where[0])//2]]
# create the adjacency matrix based on the selected thresold
adj_mat = np.zeros((k,k))
adj_mat[matrix_no_diagonal>=th] = 1
adj_mat[matrix_no_diagonal<th] = 0
# create nx graph object
G = nx.from_numpy_matrix(adj_mat)
# check number of isolates
#nx.number_of_isolates(G)
# create a dictionary of labels nodes
nodes = np.arange(0,64)
channel_names = f.getSignalLabels()
labels = dict(zip(nodes, channel_names))
# layout network choice
layout = nx.drawing.layout.random_layout(G)  
# plot network                   
nx.drawing.nx_pylab.draw_networkx(G,pos = layout,labels = labels )



