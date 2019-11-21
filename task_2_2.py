
from PDC import PDC
import numpy as np
import os

'''
TASK 2.2


Search in the literature a definition of small-worldness index (i.e. an index
describing the small-world organization of a network) and compute it.
'''

'''
Problem: Python function to implement smallworldness is just for undirected graph.

Then this code saves adjacency matrix on a csv file, then we will use R to implement the smallwordness function 
on the directed graph (see task_2_2.R)
'''


if __name__ == "__main__":

    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
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
        os.remove("data/a_matrix2.csv")
        os.remove("data/a_matrix1.csv")
        # save to csv
        np.savetxt("data/matrix2.csv", a_matrix2, delimiter=",")
        np.savetxt("data/matrix1.csv", a_matrix1, delimiter=",")

    except:
        # save to csv
        np.savetxt("data/matrix2.csv", a_matrix2, delimiter=",")
        np.savetxt("data/matrix1.csv", a_matrix1, delimiter=",")



