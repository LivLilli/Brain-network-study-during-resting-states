#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:18:39 2019

@author: livialilli
"""
import networkx as nx
from PDC import PDC
from DTF import DTF
def task_2_1(file, density, freq):
    pdc = PDC(file, freq)
    # adjacency matrix
    a_matrix = pdc.adj_matrix(density)
    # direct4ed graph
    G = nx.from_numpy_matrix(a_matrix,create_using=nx.DiGraph)
    
    ### GLOBAL INDECES
    # avarage clustering coefficient
    avg_clustering_coeff = nx.average_clustering(G)
    # avarage shortest path length
    avg_shortest_path_length = nx.average_shortest_path_length(G)
    
    ### LOCAL INDECES
    # degree dictionaries
    # for each node (0-63) return:
    # the number of edges adjacent to the node
    degree = dict(nx.degree(G))
    # the number of edges pointing to the node
    in_degree = dict(G.in_degree())
    # the number of edges pointing out of the node
    out_degree = dict(G.out_degree())
    
    ### LIST THE FIRST 10 CHANNELS for local indeces
    top_10_degree = []
    top_10_in = []
    top_10_out = []
    for i in range(10):
        # add first i channel to list
        top_10_degree.append(max(degree, key=degree.get))
        # put to zero the value
        degree[max(degree, key=degree.get)] = 0
        top_10_in.append(max(in_degree, key=in_degree.get))
        in_degree[max(in_degree, key=in_degree.get)] = 0
        top_10_out.append(max(out_degree, key=out_degree.get))
        out_degree[max(out_degree, key=out_degree.get)] =0
    
    print("Using PDC on file %s: \n"%file)
    print("The avarage clustering coefficient is: ", avg_clustering_coeff)
    print('\n')
    print("The avarage shortest path length is: ", avg_shortest_path_length)
    print('\n')
    print("The top 10 channels in terms of degree are: \n",top_10_degree)
    print('\n')
    print("The top 10 channels in terms of in-degree are: \n",top_10_in)
    print('\n')
    print("The top 10 channels in terms of out-degree are: \n",top_10_out)
    print("\n")
    print('\n')
    
def task_2_2(file, density, freq):
    pdc = PDC(file, freq)
    # adjacency matrix
    a_matrix = pdc.adj_matrix(density)
    # undirected graph (sigma want undirected) ???
    G = nx.from_numpy_matrix(a_matrix)
    small_worldness_index = nx.sigma(G, niter= 10, nrand=3,seed= 5)
    
    print("Using PDC on file %s: \n"%file)
    print("Small-Wordlness index: ", small_worldness_index)
    
def task_2_3(file, density):
    dtf = DTF(file)
    # adjacency matrix
    a_matrix = dtf.adj_matrix(density)
    # direct4ed graph
    G = nx.from_numpy_matrix(a_matrix,create_using=nx.DiGraph)
    ### GLOBAL INDECES
    # avarage clustering coefficient
    avg_clustering_coeff = nx.average_clustering(G)
    # avarage shortest path length
    avg_shortest_path_length = nx.average_shortest_path_length(G)
    
    print("Using DTF on file %s: \n"%file)
    print("The avarage clustering coefficient is: ", avg_clustering_coeff)
    print('\n')
    print("The avarage shortest path length is: ", avg_shortest_path_length)
    print('\n')

    
    
if __name__=="__main__":
    
    file1 = 'files/S003/S003R01.edf'
    file2 = 'files/S003/S003R02.edf'
    density1 = 0.20
    alpha_freq = (8,13)
    
    task_2_1(file1, density1, alpha_freq)
    task_2_1(file2, density1, alpha_freq)
    
    task_2_2(file1, density1, alpha_freq)
    task_2_2(file2, density1, alpha_freq)
    
    task_2_3(file1, density1)
    task_2_3(file2, density1)
    