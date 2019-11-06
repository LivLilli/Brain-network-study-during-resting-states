# import libraries
import numpy as np
#import mne
#import pandas as pd
#import os
import connectivipy as cp
import pyedflib

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




# reading the edf file S003R01.edf
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
# matrix A of coefficient   
A_matrix = cp.mvarmodel.Mvar.fit(data)[0]
# reflection matrix V 
V_matrix = cp.mvarmodel.Mvar.fit(data)[1]