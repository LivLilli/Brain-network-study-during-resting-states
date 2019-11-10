#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:00:30 2019

@author: livialilli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:31:34 2019

@author: livialilli
"""
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
import matplotlib.pyplot as plt
import matplotlib as mpl


class DTF(object):
    
    def __init__(self, file_name):
        # reading the edf file 
        self.f = pyedflib.EdfReader(file_name)
        #number of channels
        self.k = self.f.signals_in_file
        #number of samples 
        self.N = self.f.getNSamples()[0]
        # getting Sample Frequency of a channel (for ex 0)
        # Sample freq is the same for all our channels
        self.fs = self.f.getSampleFrequency(0)
    
    def build_data(self):
        # creating array of data 
        # rows must be channels
        # cols must be data points
        data = np.zeros((self.k, self.N))
        for i in np.arange(self.k):
            data[i, :] = self.f.readSignal(i)
            
        return data
        
    def MVar_DTF(self):
        data = self.build_data()
        # MVar model fitting on data
        # data is an array of dimension kN (k = number of channels, N = number of data points)
        # model order, when default None it estimates order using akaike order criteria.
        # mvar fitting algorithm, default Yule-Walker 
        # matrix A of coefficient   
        A_matrix = cp.mvarmodel.Mvar.fit(data)[0]
        # model order p
        # p = A_matrix.shape[0]
        # reflection matrix V 
        V_matrix = cp.mvarmodel.Mvar.fit(data)[1]
        
        # computing PDC
        # pdc_fun return an array (resolution x k x k)
        # resolution = fs/2
        dtf = cp.conn.dtf_fun(A_matrix, V_matrix, self.fs, self.fs//2)
        
        
        # extract just the matrices kxk we need, based on alpha [8,13 HZ]
        # so return 6 matrices kxk
        freq_selection = dtf[7:13]
        
        return freq_selection

    def final_dtf_matrix(self):
        freq_selection = self.MVar_DTF()
        # mean among the 6 matrices
        # return a kxk matrix 
        # each component i,j is the mean among the components i,j of the 6 matrices
        # initialize the result matrix
        mean_matrix= np.zeros((self.k,self.k))
        # return freq_selection array collapsed in 1 dimension
        flat = freq_selection.flatten()
        # for each i, compute the mean among the component of 6 matrices on same positions
        # add the mean value to our mean_matrix
        for i in range(0,self.k*self.k):
            mean = (flat[i]+flat[i+self.k*self.k]+flat[i+2*self.k*self.k]+flat[i+3*self.k*self.k]+flat[i+self.k*self.k*4]+flat[i+self.k*self.k*5])/(freq_selection.shape[0])
            mean_matrix.flat[i] = mean
        
        # we are not interested in self loops
        # then delete the diagonal
        matrix_no_diagonal = mean_matrix-np.triu(np.tril(mean_matrix))
        return matrix_no_diagonal
    
    
    def adj_matrix(self, density):
        matrix_no_diagonal = self.final_dtf_matrix()
        # choice of the Thrhesold s.t. 
        # the resulting binary connectivity matrices have network density equal to requested density.
        # grid
        thresholds = np.linspace(0.0, 1.0, 10000)
        densities = []
        # for each t compute density and add it to a list
        for t in thresholds:
            adj_mat = np.zeros((self.k,self.k))
            adj_mat[matrix_no_diagonal>=t] = 1
            adj_mat[matrix_no_diagonal<t] = 0
            graph = nx.from_numpy_matrix(adj_mat)
            densities.append(nx.density(graph))
        # convert list in array
        densities= np.asarray(densities)
        # find index position of the value that's the nearest to density value
        where = (np.abs(densities-density)).argmin()
        # select the middle index among the found ones
        # save the corresponding value of threshold
        th = thresholds[where]
        # create the adjacency matrix based on the selected thresold
        result_adj_mat = np.zeros((self.k,self.k))
        result_adj_mat[matrix_no_diagonal>=th] = 1
        result_adj_mat[matrix_no_diagonal<th] = 0

        return result_adj_mat

    def binary_heatmap(self, density, file_name):
        adj_mat = self.adj_matrix(density)
        # heatmap of the binary matrix
        fig, ax = plt.subplots()
        # define the colors
        cmap = mpl.colors.ListedColormap(['k', 'c'])
        # colors boundaries
        # black is for zeros, blues for ones
        bounds = [0., 0.5, 1.]
        # colormap based on normalized limits
        # cmap.N = number of colors
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        # plot it
        plt.title("Using DTF \n File: %s " %file_name + " Density: %f " %density)
        ax.imshow(adj_mat, interpolation='none', cmap=cmap, norm=norm)




if __name__=="__main__":
    ### TASK 1.2
    # file name
    file1 = 'files/S003/S003R01.edf'
    file2 = 'files/S003/S003R02.edf'
    # density 20%
    density1 = 0.20
    # initialize PDC class for file1
    dtf1 = DTF(file1)
    # heatmap file 1
    dtf1.binary_heatmap(density1,file1)
    # initialize PDC class for file2
    dtf2 = DTF(file2)
    # heatmap file 2
    dtf2.binary_heatmap(density1,file2)
    
    

    
    
  
        
    
    
    
    
    
    
    
    
    
    
    
    