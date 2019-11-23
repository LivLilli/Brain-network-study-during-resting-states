import pandas as pd
from PDC import PDC
import networkx as nx
import os
'''
TASK 2.6

Compare the networks obtained with the analysis 1.6 in terms of graph indices.
(the choice of this task is advised only in the case of selection of task 1.6).



----------------------

task_2_6(file, density, freq, f) :

Takes in input:

    - file: edf file name;
    
    - density: density value;
    
    - freq: rythm;
    
    - f string (for example file1) to indicate number of file.
    
Returns:
    From the computation of global indeces:
    
        - Avarage Custering Coefficient;
        
        - Avarage Shortest Path.
    
    From the computation of local indeces:
    
        - Top 10 channels in terms of degree;
        
        - Top 10 channels in terms of in-degree;
        
        - Top 10 channels in terms of out-degree.
'''



def task_2_6(file, density, freq, f) :
    # creating labels list
    table = pd.read_csv("data/channel_locations.txt", delimiter='\s+', )
    labels = list(table.label)
    for i in range(len(labels)) :
        # clean labels name
        labels[i] = labels[i].replace('..', '')
        labels[i] = labels[i].replace('.', '')
    labels_dic = dict(zip([x for x in range(len(labels))], labels))
    pdc = PDC(file, freq)
    # adjacency matrix
    a_matrix = pdc.adj_matrix(density)
    # direct4ed graph
    G = nx.from_numpy_matrix(a_matrix, create_using=nx.DiGraph)

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
    degree_df = pd.DataFrame.from_dict(degree, orient='index', columns=["Degree"])
    # the number of edges pointing to the node
    in_degree = dict(G.in_degree())
    in_degree_df = pd.DataFrame.from_dict(in_degree, orient='index', columns=["In-Degree"])
    # the number of edges pointing out of the node
    out_degree = dict(G.out_degree())
    out_degree_df = pd.DataFrame.from_dict(out_degree, orient='index', columns=["Out-Degree"])

    ### LIST THE FIRST 10 CHANNELS for local indeces
    top_10_degree = []
    top_10_in = []
    top_10_out = []
    for i in range(10) :
        # add first i channel to list
        top_10_degree.append(labels[max(degree, key=degree.get)])
        # put to zero the value
        degree[max(degree, key=degree.get)] = 0
        top_10_in.append(labels[max(in_degree, key=in_degree.get)])
        in_degree[max(in_degree, key=in_degree.get)] = 0
        top_10_out.append(labels[max(out_degree, key=out_degree.get)])
        out_degree[max(out_degree, key=out_degree.get)] = 0
    indeces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    top_10_degree_df = pd.DataFrame(top_10_degree, index=indeces, columns=['Degree'])
    top_10_in_df = pd.DataFrame(top_10_in, index=indeces, columns=['In-Degree'])
    top_10_out_df = pd.DataFrame(top_10_out, index=indeces, columns=['Out-Degree'])

    # save top 10 to file csv
    top_10_df = pd.concat([top_10_degree_df, top_10_in_df, top_10_out_df], axis=1)
    try :
        os.remove('results/task_2_6_ %s' % f + '_top_10.csv')
        top_10_df.to_csv('results/task_2_6_ %s' % f + '_top_10.csv')
    except :
        top_10_df.to_csv('results/task_2_6_ %s' % f + '_top_10.csv')

    # save all degree on csv
    all_degree_df = pd.concat([degree_df, in_degree_df, out_degree_df], axis=1)
    all_degree_df = all_degree_df.rename(index=labels_dic)
    try :
        os.remove('results/task_2_6_%s' % f + '_all_degree.csv')
        all_degree_df.to_csv('results/task_2_6_%s' % f + '_all_degree.csv')
    except :
        all_degree_df.to_csv('results/task_2_6_%s' % f + '_all_degree.csv')

    # save global indeces to file txt
    try :
        os.remove('results/task_2_6_%s' % f + '_global.txt')
        text_file = open('results/task_2_6_%s' % f + '_global.txt', "w")
        text_file.write("Avarage Clustering Coefficient: %f \n \n" % avg_clustering_coeff)
        text_file.write("Avarage Shortest Path: %f" % avg_shortest_path_length)
        text_file.close()
    except :
        text_file = open('results/task_2_6_%s' % f + '_global.txt', "w")
        text_file.write("Avarage Clustering Coefficient: %f \n \n" % avg_clustering_coeff)
        text_file.write("Avarage Shortest Path: %f" % avg_shortest_path_length)
        text_file.close()
    print("Done!")



if __name__=="__main__":
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    f1 = 'file1'
    f2 = 'file2'
    # density 20%
    density1 = 0.20
    # theta rythm
    theta_range = (4,7)
    
    
    task_2_6(file1, density1, theta_range,f1)
    task_2_6(file2, density1, theta_range,f2)
    
    
