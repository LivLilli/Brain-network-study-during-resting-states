#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import libraries
import numpy as np
import connectivipy as cp
import pyedflib
import warnings
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Filter out warnings
warnings.filterwarnings("ignore", category=FutureWarning)

'''
sub_PDC() class 

Compute PDC on just a subset of channels.

Make a graphical representation of the network, using given Cartesian coordinates

'''


# class takes in inputs:
# .edf file name
# list of channels subset (in our task they are 19)
# .txt file name
# density
class SubPDC(object):

    def __init__(self, file_edf_name, subset_channel, file_txt_name, density):
        self.edf_file = file_edf_name
        # reading the edf file 
        self.f = pyedflib.EdfReader(self.edf_file)
        # number of channels
        self.k = self.f.signals_in_file
        # number of samples
        self.N = self.f.getNSamples()[0]
        # getting Sample Frequency of a channel (for ex 0)
        # Sample freq is the same for all our channels
        self.fs = self.f.getSampleFrequency(0)
        self.labels = self.f.getSignalLabels()
        self.subset_channel = subset_channel
        self.new_k = len(self.subset_channel)
        self.txt_name = file_txt_name
        self.density = density

    def build_data(self):
        # creating array of data 
        # rows must be channels
        # cols must be data points
        data = np.zeros((self.k, self.N))
        for i in np.arange(self.k):
            data[i, :] = self.f.readSignal(i)

        return data

    def sub_data(self):
        data = self.build_data()
        # initialize empty list of 19 channels indeces
        indeces_19 = []
        # for each channel label
        for i in range(self.k):
            # clean labels name
            self.labels[i] = self.labels[i].replace('..','')
            self.labels[i] = self.labels[i].replace('.','')
            # if label name is a 19 channel
            if self.labels[i] in self.subset_channel:
                # save its index
                indeces_19.append(i)

        # data of the 19 channels
        data_19 = data[indeces_19]
        # return new data (19 channels) 
        # and indeces of 19 channels in our data 
        return data_19, indeces_19

    def mvar_dpc(self):
        data, idx = self.sub_data()
        # MVar model fitting on data
        # data is an array of dimension kN (k = number of channels, N = number of data points)
        # model order, when default None it estimates order using akaike order criteria.
        # mvar fitting algorithm, default Yule-Walker 
        # matrix A of coefficient   
        a_matrix = cp.mvarmodel.Mvar.fit(data)[0]
        # model order p
        # p = A_matrix.shape[0]
        # reflection matrix V 
        v_matrix = cp.mvarmodel.Mvar.fit(data)[1]

        # computing PDC
        # pdc_fun return an array (resolution x k x k)
        # resolution = fs/2
        pdc = cp.conn.pdc_fun(a_matrix, v_matrix, self.fs, self.fs//2)

        # extract just the matrices kxk we need, based on alpha [8,13 HZ]
        # so return 6 matrices kxk
        freq_selection = pdc[7:13]

        return freq_selection, idx

    def final_pdc_matrix(self):
        freq_selection,idx = self.mvar_dpc()
        # mean among the 6 matrices
        # return a kxk matrix 
        # each component i,j is the mean among the components i,j of the 6 matrices
        mean_matrix = np.mean(freq_selection, 0)

        # we are not interested in self loops
        # then delete the diagonal
        matrix_no_diagonal = mean_matrix-np.triu(np.tril(mean_matrix))
        return matrix_no_diagonal,idx

    def adj_matrix(self):
        matrix_no_diagonal,idx = self.final_pdc_matrix()
        # choice of the Thrhesold s.t. 
        # the resulting binary connectivity matrices have network density equal to requested density.
        # grid
        thresholds = np.linspace(0.0, 1.0, 10000)
        densities = []
        # for each t compute density and add it to a list
        for t in thresholds:
            adj_mat = np.zeros((self.new_k, self.new_k))
            adj_mat[matrix_no_diagonal >= t] = 1
            adj_mat[matrix_no_diagonal < t] = 0
            graph = nx.from_numpy_matrix(adj_mat,create_using=nx.DiGraph)
            densities.append(nx.density(graph))
        # convert list in array
        densities = np.asarray(densities)
        # find index position of the value that's the nearest to density value
        where = (np.abs(densities-self.density)).argmin()
        # select the middle index among the found ones
        # save the corresponding value of threshold
        th = thresholds[where]
        # create the adjacency matrix based on the selected thresold
        result_adj_mat = np.zeros((self.new_k, self.new_k))
        result_adj_mat[matrix_no_diagonal >= th] = 1
        result_adj_mat[matrix_no_diagonal < th] = 0

        return result_adj_mat,idx

    def open_file_txt(self):
        # delimiter: multiple spaces
        table=pd.read_csv(self.txt_name, delimiter='\s+')
        # list of x coord
        coord_x = list(table.x)
        # list of y coord
        coord_y = list(table.y)
        # list of coord tuple (x,y)
        coord_list = []
        for x,y in zip(coord_x, coord_y):
            coord_list.append((x,y))
        # list of indexes from 0 to 64
        indexes = list(range(0,self.k))
        # dictionary of coordinates
        # keys from 0 to 64
        coord_dic = dict(zip(indexes, coord_list))

        return coord_dic

    def graph(self):
        # dict of coordinates
        coord_dic = self.open_file_txt()
        # adj matrix and positional indeces of 19 channels 
        adj_mat, idx_19 = self.adj_matrix()
        # nx graph
        # create_using = DiGraph for directed graph
        G = nx.from_numpy_matrix(adj_mat,create_using=nx.DiGraph)
        # coord of just the 19 channels
        # keys = positional indeces of 19 channels in the all channels list
        coord_dic_19 = dict((k, coord_dic[k]) for k in idx_19)
        # coord_dic_19 keys
        old_keys = list(coord_dic_19.keys())
        # for each key of coord_dic_19
        for i in range(len(idx_19)):
            # convert old key in index from 0 to 18
            coord_dic_19[i] =coord_dic_19.pop(old_keys[i])
        # create a dictionary of labels nodes
        nodes = np.arange(0,len(idx_19))
        channel_names = self.subset_channel
        labels_dic = dict(zip(nodes, channel_names))
        # print number of edges
        print("NUMBER OF EDGES  ", nx.Graph.number_of_edges(G))
        # draw graph
        plt.title("Using PDC \n File: %s " %self.edf_file + " Density: %f " %self.density)
        nx.draw_networkx_nodes(G, pos=coord_dic_19, node_color='cyan')
        nx.draw_networkx_edges(G, pos=coord_dic_19, arrowstyle='->', arrowsize=10, width=2)

        nx.draw_networkx(G, pos=coord_dic_19, labels=labels_dic, node_size=500, node_color="cyan")


if __name__ == "__main__":
    ### TASK 1.5
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    txt_file = 'data/channel_locations.txt'
    # advised density 5%
    density1 = 0.05
    # 19 channels
    channels_19 = {"Fp1", "Fp2", "F7", 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3',
                   'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2'}

    # initialize PDC class for file1
    pdc1 = SubPDC(file1, channels_19, txt_file, density1)
    # initialize PDC class for file2
    pdc2 = SubPDC(file2, channels_19, txt_file, density1)

    pdc1.graph()
    plt.show()
    pdc2.graph()
    plt.show()










