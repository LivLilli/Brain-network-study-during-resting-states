
from PDC import PDC
import numpy as np
import os
import networkx as nx
'''
TASK 2.2


Search in the literature a definition of small-worldness index (i.e. an index
describing the small-world organization of a network) and compute it.

------------

Here we save our adjacency matrices on csv files and we compute the small-worldness coefficient on R (see task_2_2.R).
'''

if __name__ == "__main__":

    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    f1 = 'file1'
    f2 = 'file2'
    density1 = 0.20
    alpha_freq = (8,13)

    pdc1= PDC(file1, alpha_freq)
    # adjacency matrix
    a_matrix1 = pdc1.adj_matrix(density1)

    pdc2 = PDC(file2, alpha_freq)
    # adjacency matrix
    a_matrix2 = pdc2.adj_matrix(density1)

    try:
        # delete existing file
        os.remove("data/matrix2.csv")
        os.remove("data/matrix1.csv")
        # save to csv
        np.savetxt("data/matrix2.csv", a_matrix2, delimiter=",")
        np.savetxt("data/matrix1.csv", a_matrix1, delimiter=",")

    except:
        # save to csv
        np.savetxt("data/matrix2.csv", a_matrix2, delimiter=",")
        np.savetxt("data/matrix1.csv", a_matrix1, delimiter=",")


    #G_und1 = nx.from_numpy_matrix(a_matrix1, create_using=nx.Graph)
    #G_und2 = nx.from_numpy_matrix(a_matrix2, create_using=nx.Graph)

    #print(nx.smallworld.sigma(G_und1))
    #small_worldness(G_und1, f1)
    #small_worldness(G_und2, f2)