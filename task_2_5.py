#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:17:47 2019

@author: livialilli
"""
'''
Make a topographical representation of local indices.

Represent graph with nodes dimesnion depending on their:
    * in-degree
    * out-degree
    * degree
'''
from PDC import PDC
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (14,14)

def open_file_txt(file):
    # delimiter: multiple spaces
    table=pd.read_csv(file,delimiter='\s+')
    # list of x coord
    coord_x = list(table.x)
    # list of y coord
    coord_y = list(table.y)
    # list of labels
    labels_list = list(table.label)
    for i in range(len(coord_x)):
        # clean labels name
        labels_list[i] = labels_list[i].replace('..','')
        labels_list[i] = labels_list[i].replace('.','')
    # list of coord tuple (x,y)
    coord_list = []
    for x,y in zip(coord_x, coord_y):
        coord_list.append((x,y))
    # list of indexes from 0 to 64
    indexes = list(range(0,len(coord_x)))
    # dictionary of coordinates
    # keys from 0 to 64
    coord_dic = dict(zip(indexes, coord_list))    
    
    return coord_dic, labels_list



def task_2_5(file, density, freq):
    pdc = PDC(file, freq)
    # adjacency matrix
    a_matrix = pdc.adj_matrix(density)
    # direct4ed graph
    G = nx.from_numpy_matrix(a_matrix,create_using=nx.DiGraph)
    
    coord_dic,labels_list = open_file_txt("channel_locations.txt")
    
    ### LOCAL INDECES
    # degree dictionaries
    # for each node (0-63) return:
    # the number of edges adjacent to the node
    degree = dict(nx.degree(G))
    # the number of edges pointing to the node
    in_degree = dict(G.in_degree())
    # the number of edges pointing out of the node
    out_degree = dict(G.out_degree())
    
    # dictionary of labels
    nodes = np.arange(0,len(a_matrix))
    channel_names = labels_list
    labels_dic = dict(zip(nodes, channel_names))    
    
    
    plt.title("Using PDC \n File: %s " %file + " Density: %f \n\n" %density + "Degree Rapresentation")
    nx.draw_networkx_nodes(G, pos=coord_dic, node_color='cyan')
    nx.draw_networkx_edges(G, pos=coord_dic, arrowstyle='->',
                               arrowsize=10,width=2)

    nx.draw_networkx(G, pos=coord_dic,labels =labels_dic,nodelist = list(labels_dic.keys()),node_size=[v * 100 for v in degree.values()],node_color="cyan")       
    plt.show()
    
    plt.title("Using PDC \n File: %s " %file + " Density: %f \n\n" %density +"IN-Degree Rapresentation")
    nx.draw_networkx_nodes(G, pos=coord_dic, node_color='cyan')
    nx.draw_networkx_edges(G, pos=coord_dic, arrowstyle='->',
                               arrowsize=10,width=2)

    nx.draw_networkx(G, pos=coord_dic,labels =labels_dic,nodelist = list(labels_dic.keys()),node_size=[v * 100 for v in in_degree.values()],node_color="cyan")       
    plt.show()
    
    plt.title("Using PDC \n File: %s " %file + " Density: %f \n\n" %density +"OUT-Degree Rapresentation")
    nx.draw_networkx_nodes(G, pos=coord_dic, node_color='cyan')
    nx.draw_networkx_edges(G, pos=coord_dic, arrowstyle='->',
                               arrowsize=10,width=2)

    nx.draw_networkx(G, pos=coord_dic,labels =labels_dic,nodelist = list(labels_dic.keys()),node_size=[v * 100 for v in out_degree.values()],node_color="cyan")       
    plt.show()


if __name__=="__main__":
    
    file1 = 'files/S003/S003R01.edf'
    file2 = 'files/S003/S003R02.edf'
    density1 = 0.05
    alpha_freq = (8,13)
    
    task_2_5(file1,density1,alpha_freq)
    task_2_5(file2,density1,alpha_freq)
     
