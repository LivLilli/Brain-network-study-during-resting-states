from PDC import PDC
import networkx as nx
import pandas as pd

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
    '''
    print("Using PDC on file %s:  "%file, "   Density: %f"%density)
    
    print("The avarage clustering coefficient is: ", avg_clustering_coeff)
    print('\n')
    print("The avarage shortest path length is: ", avg_shortest_path_length)
    print('\n')    
    '''
    return avg_clustering_coeff, avg_shortest_path_length

'''
create_csv_file(c_10,c_30,c_50,s_10,s_30,s_50, f):

    Takes in input:
    
        - c_10, c_30 c_50 = avarage clustering coefficients of network at densities at 10%, 30%, 50%;

        - s_10, s_30, s_50 = avarage shortest path of  network at densities at 10%, 30%, 50%.

    Returns:
    
        - save dataframe of results on txt file.
'''
def create_csv_file(c_10,c_30,c_50,s_10,s_30,s_50, f):
    cluster_dic = {'Avg_Clustering_Coeff': [c_10, c_30, c_50]}
    path_dic = {'Avg_Shortest_Path': [s_10, s_30,s_50]}
    cluster_df = pd.DataFrame.from_dict(cluster_dic,orient='index', columns = ["Density 10%", 'Density 30%', 'Density 50%'])
    path_df = pd.DataFrame.from_dict(path_dic,orient='index', columns = ["Density 10%", 'Density 30%', 'Density 50%'])
    result = pd.concat([cluster_df, path_df], axis = 0)
    try :
        os.remove('results/task_2_4_%s' % f + '.csv')
        result.to_csv('results/task_2_4_%s' % f + '.csv')
    except :
        result.to_csv('results/task_2_4_%s' % f + '.csv')



if __name__=="__main__":
    ### TASK 1.1
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # alpha rythm
    alpha_freq = (8,13)
    f1 = 'file1'
    f2 = 'file2'
    ### density 1% :GRAPH NOT WEAKLY CONNECTED
    ### density 5% :GRAPH NOT WEAKLY CONNECTED
    
    ### density 10%
    density1 = 0.10
    # using PDC
    c_file1_10, s_file1_10 = task_2_4(file1, density1, alpha_freq)
    c_file2_10, s_file2_10 = task_2_4(file2, density1, alpha_freq)

    
    
    ### density 30%
    density2 = 0.30
    # using PDC
    c_file1_30, s_file1_30 = task_2_4(file1, density2, alpha_freq)
    c_file2_30, s_file2_30 = task_2_4(file2, density2, alpha_freq)

    
    
    ### density 50%
    density3 = 0.50
    c_file1_50, s_file1_50 = task_2_4(file1, density3, alpha_freq)
    c_file2_50, s_file2_50 = task_2_4(file2, density3, alpha_freq)

    ### saving on csv file
    create_csv_file(c_file1_10,c_file1_30, c_file1_50, s_file1_10,s_file1_30,s_file1_50,f1)
    create_csv_file(c_file2_10, c_file2_30, c_file2_50, s_file2_10, s_file2_30, s_file2_50, f2)
