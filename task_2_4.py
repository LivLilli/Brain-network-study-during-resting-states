from PDC import PDC
import networkx as nx


'''
TASK 2.4

Study the behaviour of global graph indices in function of network density (see
point 2.3 for density values).
the choice of this task is advised in the case of selection of task 1.3).                                                                        

---------------------

task_2_4(file, density, freq)

Takes in input:

    - edf file name;

    - density value;
    
    - frequency range (rythm).
    
Returns:

    - Avg Clustering Coefficient;
    
    - Avg Shortest Path.
'''

def task_2_4(file, density, freq):
    pdc = PDC(file, freq)
    # adjacency matrix
    a_matrix = pdc.adj_matrix(density)
    # directed graph
    G = nx.from_numpy_matrix(a_matrix,create_using=nx.DiGraph)
    
    ### GLOBAL INDECES
    # avarage clustering coefficient
    avg_clustering_coeff = nx.average_clustering(G)
    # avarage shortest path length
    avg_shortest_path_length = nx.average_shortest_path_length(G)
    print("Using PDC on file %s:  "%file, "   Density: %f"%density)
    
    print("The avarage clustering coefficient is: ", avg_clustering_coeff)
    print('\n')
    print("The avarage shortest path length is: ", avg_shortest_path_length)
    print('\n')    



if __name__=="__main__":
    ### TASK 1.1
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # alpha rythm
    alpha_freq = (8,13)
    
    ### density 1% :GRAPH NOT WEAKLY CONNECTED
    ### density 5% :GRAPH NOT WEAKLY CONNECTED
    
    ### density 10%
    density1 = 0.10
    # using PDC
    task_2_4(file1, density1, alpha_freq)
    task_2_4(file2, density1, alpha_freq)

    
    
    ### density 30%
    density2 = 0.30
    # using PDC
    task_2_4(file1, density2, alpha_freq)
    task_2_4(file2, density2, alpha_freq)

    
    
    ### density 50%
    density3 = 0.50
    task_2_4(file1, density3, alpha_freq)
    task_2_4(file2, density3, alpha_freq)


    