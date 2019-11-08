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


'''
# read edf files
edf1 = mne.io.read_raw_edf('files/S003/S003R01.edf')
edf2 = mne.io.read_raw_edf('files/S003/S003R02.edf')

# join respect to ';'
header1 = ','.join(edf1.ch_names)
header2 = ','.join(edf2.ch_names)


# drop existing csv file
os.remove('S003R01.csv')
os.remove('S003R02.csv')

# save csv file
np.savetxt('S003R01.csv', edf1.get_data().T, delimiter=',', header=header1)
np.savetxt('S003R02.csv', edf2.get_data().T, delimiter=',', header=header2)

#reading as df
df1 = pd.read_csv('S003R01.csv', sep=',')
df2 = pd.read_csv('S003R02.csv', sep=',')
'''


'''
def pdc_computation(file_name):
    # reading the edf file 
    f = pyedflib.EdfReader(file_name)
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
    #resolution = ???
    pdc = cp.conn.pdc_fun(A_matrix, V_matrix, fs, 80)
    
    return pdc

pdc_1 = pdc_computation('files/S003/S003R01.edf')

pdc_2 = pdc_computation('files/S003/S003R02.edf')

'''

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
# select frequency of alpha rythm [8,13]
alpha = range(7,12)
# extract just the matrices kxk we need, based on alpha
# then return 6 matrices kxk
freq_selection = pdc[7:13]
# mean among the 6 matrices
# return a kxk matrix where each component i,j is the mean among the components i,j of the 6 matrices

# initialize the result matrix
mean_matrix= np.zeros((k,k))
# return freq_selection array collapsed in 1 dimension
flat = freq_selection.flatten()
# for each i, compute the mean among the component of 6 matrices on same positions
for i in range(0,k*k):
    mean = (flat[i]+flat[i+k*k]+flat[i+2*k*k]+flat[i+3*k*k]+flat[i+k*k*4]+flat[i+k*k*5])/(freq_selection.shape[0])
    mean_matrix.flat[i] = mean




'''
graph = nx.from_numpy_matrix(adj_matrix)
density = nx.density(graph)
'''