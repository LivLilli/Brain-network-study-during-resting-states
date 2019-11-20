#!/usr/bin/env python

import networkx as nx
from PDC import PDC
import community
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
Determine number and composition (i.e. list of nodes) of the communities
obtained applying one of the algorithms introduced during the course.

Make a graphical representation of the community structure in both rest conditions.


'''

def task_4_1(file, freq):
    pdc = PDC(file, freq)
    weighted_matrix  = pdc.final_pdc_matrix()
    G = nx.from_numpy_matrix(weighted_matrix)
    ### USING NETWORKX
    # PROBLEM: it accepts just undirected graphs
    
    # dictionary: for each node the corresponding community
    # best_partition: compute the partition of the graph nodes which maximises the modularity using the Louvain heuristices
    comm_dic = dict(community.best_partition(G))
    # communities found
    values = set(list(comm_dic.values()))
    print('Using PDC   File:%s' % file)
    print('Number of communities: ', len(values))
    print('Communities composition: ', comm_dic)
    return comm_dic,values



def open_file_txt(file):
    # delimiter: multiple spaces
    table = pd.read_csv(file, delimiter='\s+')
    # list of x coord
    coord_x = list(table.x)
    # list of y coord
    coord_y = list(table.y)
    # list of labels
    labels_list = list(table.label)
    for i in range(len(coord_x)):
        # clean labels name
        labels_list[i] = labels_list[i].replace('..', '')
        labels_list[i] = labels_list[i].replace('.', '')
    # list of coord tuple (x,y)
    coord_list = []
    for x, y in zip(coord_x, coord_y):
        coord_list.append((x, y))
    # list of indexes from 0 to 64
    indexes = list(range(0, len(coord_x)))
    # dictionary of coordinates
    # keys from 0 to 64
    coord_dic = dict(zip(indexes, coord_list))
    # dictionary of labels
    nodes = np.arange(0,len(coord_dic))
    labels_dic = dict(zip(nodes, labels_list))


    return coord_dic, labels_dic



def task_4_2(comm, part, file, freq):
    pdc = PDC(file,freq)
    weighted_matrix = pdc.final_pdc_matrix()
    G = nx.from_numpy_matrix(weighted_matrix)
    pos,labels_dic = open_file_txt("data/channel_locations.txt")
    size = len(comm)
    count = 0
    colour = [ "purple", "orange", "red", "green", "white", "black" ]
    plt.title("Using PDC   File:%s \n" % file)
    for com in comm:
        count = count + 1
        list_nodes = [nodes for nodes in part.keys()
                                    if part[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                    node_color = colour[com])


    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()


if __name__=="__main__":

    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    alpha_freq = (8, 13)

    partition1, communities1 = task_4_1(file1,alpha_freq)
    partition2, communities2 = task_4_1(file2,alpha_freq)
    task_4_2(communities1,partition1,file1,alpha_freq)
    task_4_2(communities2,partition2,file2,alpha_freq)

