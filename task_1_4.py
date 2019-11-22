
import connectivipy as cp
import numpy as np
from connectivipy import mvar_gen
import pyedflib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

'''
TASK 1.4

Considering the subset of 19 channels suggested in Figure 1 and Table 2, estimate

the connectivity using PDC or DTF and apply a statistical validation method 
(asymptotic statistics7, resampling procedure8,...) to filter out values that are not significantly different from 0 
(𝑃𝐷𝐶(𝑖, 𝑗) ≠ 0 𝑤𝑖𝑡h 𝑝 < 5%).
'''


class SV(object):

    def __init__(self, file_edf_name, subset_channel, file_txt_name):

        '''
            - file_edf_name: edf file name string
            - subset_channel: list of channels to consider
            - file_txt_name: txt file name string of coordinates
            - density: density value
        '''

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


    def build_data(self):

        '''
        Returns:
            array of data:
            rows must be channels and cols must be data points
        '''

        data = np.zeros((self.k, self.N))
        for i in np.arange(self.k):
            data[i, :] = self.f.readSignal(i)

        return data

    def sub_data(self):

        '''
        Returns:

             - array of data of the channels subset considered

             - list of positional indeces of subset channels inside the list of all channels
        '''

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
        return data_19,indeces_19
    def s(self):
        table = pd.read_csv(self.txt_name, delimiter='\s+', )
        labels = list(table.label)
        for i in range(len(labels)) :
            # clean labels name
            labels[i] = labels[i].replace('..', '')
            labels[i] = labels[i].replace('.', '')

        sub_data,idx_19 = self.sub_data()
        labels_19= [labels[i] for i in idx_19]
        data = cp.Data(sub_data,fs=self.fs, chan_names=labels)
        data.fit_mvar()
        pdc_values = data.conn('pdc')
        s_matrix= data.significance(Nrep=200, alpha=0.05)
        return s_matrix

    def adjacency_matrix(self):
        s_matrix = self.s()
        adj_matrix = np.zeros((len(s_matrix), len(s_matrix)))
        adj_matrix[s_matrix >= 0.05] = 0
        adj_matrix[s_matrix < 0.05] = 1

        return adj_matrix

    def binary_heatmap(self):

        '''
        Returns:
            binary heatmap of adjacency matrix.
        '''

        adj_mat = self.adjacency_matrix()
        # heatmap of the binary matrix
        fig, ax = plt.subplots()
        # define the colors
        cmap = mpl.colors.ListedColormap(['k', 'y'])
        # colors boundaries
        # black is for zeros, blues for ones
        bounds = [0., 0.5, 1.]
        # colormap based on normalized limits
        # cmap.N = number of colors
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

        # plot it
        plt.title("Using: PDC  \n File: %s " %self.edf_file)
        ax.set_xticks(np.arange(len(adj_mat)))
        ax.set_yticks(np.arange(len(adj_mat)))
        ax.set_xticklabels(self.subset_channel)
        ax.set_yticklabels(self.subset_channel)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")
        ax.imshow(adj_mat, interpolation='none', cmap=cmap, norm=norm)
        plt.show()

if __name__ == "__main__":
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    txt_file = 'data/channel_locations.txt'

    # 19 channels
    channels_19 = {"Fp1", "Fp2", "F7", 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3',
                   'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2'}


    sv1 = SV(file1, channels_19,txt_file)
    sv2 = SV(file2, channels_19, txt_file)
    sv1.binary_heatmap()
    plt.show()
    sv2.binary_heatmap()
    plt.show()