from PDC import PDC
import networkx as nx


'''
TASK 2.7

 Perform point 2.1 considering the weighted version of the graph indices definitions

------------------------------------------------

task_2_7(file, density, freq)

Takes in input:

    - edf file name;
    
    - density value;
    
    - frequency range (rythm).
    
Returns:

    - Avg Clustering Coefficient;
    
    - Avg Shortest Path Coefficient;
    
    - Top 10 channels in terms of degree;
    
    - Top 10 channels in terms of in-degree;
    
    - Top 10 channels in terms of out-degree.
'''



def task_2_7(file, density, freq):
    pdc = PDC(file, freq)
    # weighted adjacency matrix
    weighted_matrix  = pdc.final_pdc_matrix()
    # directed graph
    G = nx.from_numpy_matrix(weighted_matrix,create_using=nx.DiGraph)

    ### GLOBAL INDECES
    # avarage clustering coefficient
    avg_clustering_coeff = nx.average_clustering(G,weight='weight')
    # avarage shortest path length
    avg_shortest_path_length = nx.average_shortest_path_length(G,weight='weight')
    
    ### LOCAL INDECES
    # degree dictionaries
    # for each node (0-63) return:
    # the number of edges adjacent to the node
    degree = dict(nx.degree(G, weight='weight'))
    
    # the number of edges pointing to the node
    in_degree = dict(G.in_degree(weight='weight'))
    # the number of edges pointing out of the node
    out_degree = dict(G.out_degree(weight='weight'))
    
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
    
    print("Using PDC on file %s:  "%file, "   Density: %f \n"%density)
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
    
if __name__=="__main__":
    
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    density1 = 0.20
    alpha_freq = (8,13)
    
    task_2_7(file1, density1, alpha_freq)
    task_2_7(file2, density1, alpha_freq)