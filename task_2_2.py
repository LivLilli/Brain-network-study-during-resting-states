
from PDC import PDC
import numpy as np
import os
import networkx as nx
'''
TASK 2.2


Search in the literature a definition of small-worldness index (i.e. an index
describing the small-world organization of a network) and compute it.
'''

'''
small_worldness(G, f)

Takes in input:

    - Networkx Undirected Graph;
    
    - file flag 
    
Returns:

    - Small-Worldness coefficient of the network
'''


def small_worldness(G, f) :
    sw = nx.smallworld.sigma(G)

    try :
        os.remove('results/task_2_2_%s' % f + '_global.txt')
        text_file = open('results/task_2_2_%s' % f + '_smallworldness.txt', "w")
        text_file.write("Small-Worldness coefficient: %f \n \n" % sw)
        text_file.close()
    except :
        text_file = open('results/task_2_2_%s' % f + '_smallworldness.txt', "w")
        text_file.write("Small-Worldness coefficient: %f \n \n" % sw)
        text_file.close()
    print("Done!")


if __name__ == "__main__":

    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    f1 = 'file1'
    f2 = 'file2'
    density1 = 1
    alpha_freq = (8,13)

    pdc1= PDC(file1, alpha_freq)
    # adjacency matrix
    a_matrix1 = pdc1.adj_matrix(density1)

    pdc2 = PDC(file2, alpha_freq)
    # adjacency matrix
    a_matrix2 = pdc2.adj_matrix(density1)

    G_und1 = nx.from_numpy_matrix(a_matrix1, create_using=nx.Graph)
    G_und2 = nx.from_numpy_matrix(a_matrix2, create_using=nx.Graph)
    print(nx.smallworld.sigma(G_und1))
    #small_worldness(G_und1, f1)
    #small_worldness(G_und2, f2)