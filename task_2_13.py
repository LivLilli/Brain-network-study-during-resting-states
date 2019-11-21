import networkx as nx
from PDC import PDC
from task_1_2 import DTF
import pandas as pd


'''
TASK 2.1

Compute binary global (clustering coefficient, path length) and local (degree,
in/out-degree) graph indices. List the highest 10 channels for local indices.



-----------------------------------






task_2_1(file, density, freq)

Takes in input:

    - file: edf file name
    
    - density: density value
    
    - freq: rythm
    
Returns:
    From the computation of global indeces:
    
        - Avarage Custering Coefficient;
        
        - Avarage Shortest Path.
    
    From the computation of local indeces:
    
        - Top 10 channels in terms of degree;
        
        - Top 10 channels in terms of in-degree;
        
        - Top 10 channels in terms of out-degree;
'''

def task_2_1(file, density, freq):
    #creating labels list
    table=pd.read_csv("data/channel_locations.txt", delimiter='\s+', )
    labels = list(table.label)
    for i in range(len(labels)) :
    # clean labels name
        labels[i] = labels[i].replace('..', '')
        labels[i] = labels[i].replace('.', '')
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
    nodes_list = list(degree.keys())
    degree_df = pd.DataFrame.from_dict(degree, orient='index')
    # the number of edges pointing to the node
    in_degree = dict(G.in_degree())
    in_degree_df = pd.DataFrame.from_dict(in_degree,orient='index')
    # the number of edges pointing out of the node
    out_degree = dict(G.out_degree())
    out_degree_df = pd.DataFrame.from_dict(out_degree,orient='index')
    
    ### LIST THE FIRST 10 CHANNELS for local indeces
    top_10_degree = []
    top_10_in = []
    top_10_out = []
    for i in range(10):
        # add first i channel to list
        top_10_degree.append(labels[max(degree, key=degree.get)])
        # put to zero the value
        degree[max(degree, key=degree.get)] = 0
        top_10_in.append(labels[max(in_degree, key=in_degree.get)])
        in_degree[max(in_degree, key=in_degree.get)] = 0
        top_10_out.append(labels[max(out_degree, key=out_degree.get)])
        out_degree[max(out_degree, key=out_degree.get)] =0
    indeces = [1,2,3,4,5,6,7,8,9,10]
    top_10_degree_df = pd.DataFrame(top_10_degree,index=indeces, columns=['Channel'])
    top_10_in_df = pd.DataFrame(top_10_in,index=indeces,columns=['Channel'])
    top_10_out_df = pd.DataFrame(top_10_out, index=indeces,columns=['Channel'])

    print("Using PDC on file %s:  "%file, "   Density: %f \n"%density)
    print("The avarage clustering coefficient is: ", avg_clustering_coeff)
    print('\n')
    print("The avarage shortest path length is: ", avg_shortest_path_length)
    print('\n')
    print("The top 10 channels in terms of degree are: \n",top_10_degree_df)
    print('\n')
    print("The top 10 channels in terms of in-degree are: \n",top_10_in_df)
    print('\n')
    print("The top 10 channels in terms of out-degree are: \n",top_10_out_df)
    print("\n")
    print("\n")

    


'''
TASK 2.3

Compare the global indices extracted from PDC and DTF connectivity estimations.


---------------------------------




task_2_3(file, density)

Takes in input:

    - edf file name;
    
    - density value.
    
Returns:

    The computation of global indeces:
    
        - Avarage Custering Coefficient;
        
        - Avarage Shortest Path.
'''

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
    
    print("Using DTF on file %s: "%file, "   Density: %f \n"%density)
    print("The avarage clustering coefficient is: ", avg_clustering_coeff)
    print('\n')
    print("The avarage shortest path length is: ", avg_shortest_path_length)
    print('\n')

    
    
if __name__=="__main__":
    
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    density1 = 0.20
    alpha_freq = (8,13)
    
    task_2_1(file1, density1, alpha_freq)
    task_2_1(file2, density1, alpha_freq)

    task_2_3(file1, density1)
    task_2_3(file2, density1)
    