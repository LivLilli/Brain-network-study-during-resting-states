import pandas as pd
from PDC import PDC
import networkx as nx
import os

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



def task_2_7(file, density, freq,f):
    # creating labels list
    table = pd.read_csv("data/channel_locations.txt", delimiter='\s+', )
    labels = list(table.label)
    for i in range(len(labels)) :
        # clean labels name
        labels[i] = labels[i].replace('..', '')
        labels[i] = labels[i].replace('.', '')
    labels_dic = dict(zip([x for x in range(len(labels))], labels))

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
    degree_df = pd.DataFrame.from_dict(degree, orient='index', columns=["Degree"])
    # the number of edges pointing to the node
    in_degree = dict(G.in_degree(weight='weight'))
    in_degree_df = pd.DataFrame.from_dict(in_degree, orient='index', columns=["In-Degree"])
    # the number of edges pointing out of the node
    out_degree = dict(G.out_degree(weight='weight'))
    out_degree_df = pd.DataFrame.from_dict(out_degree, orient='index', columns=["Out-Degree"])
    
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
    indeces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    top_10_degree_df = pd.DataFrame(top_10_degree, index=indeces, columns=['Degree'])
    top_10_in_df = pd.DataFrame(top_10_in, index=indeces, columns=['In-Degree'])
    top_10_out_df = pd.DataFrame(top_10_out, index=indeces, columns=['Out-Degree'])
    
    # save top 10 to file csv
    top_10_df = pd.concat([top_10_degree_df, top_10_in_df, top_10_out_df], axis=1)
    try :
        os.remove('results/task_2_7_ %s' % f + '_top_10.csv')
        top_10_df.to_csv('results/task_2_7_ %s' % f + '_top_10.csv')
    except :
        top_10_df.to_csv('results/task_2_7_ %s' % f + '_top_10.csv')

    # save all degree on csv
    all_degree_df = pd.concat([degree_df, in_degree_df, out_degree_df], axis=1)
    all_degree_df = all_degree_df.rename(index=labels_dic)
    try :
        os.remove('results/task_2_7_%s' % f + '_all_degree.csv')
        all_degree_df.to_csv('results/task_2_7_%s' % f + '_all_degree.csv')
    except :
        all_degree_df.to_csv('results/task_2_7_%s' % f + '_all_degree.csv')

    # save global indeces to file txt
    try :
        os.remove('results/task_2_7_%s' % f + '_global.txt')
        text_file = open('results/task_2_7_%s' % f + '_global.txt', "w")
        text_file.write("Avarage Clustering Coefficient: %f \n \n" % avg_clustering_coeff)
        text_file.write("Avarage Shortest Path: %f" % avg_shortest_path_length)
        text_file.close()
    except :
        text_file = open('results/task_2_7_%s' % f + '_global.txt', "w")
        text_file.write("Avarage Clustering Coefficient: %f \n \n" % avg_clustering_coeff)
        text_file.write("Avarage Shortest Path: %f" % avg_shortest_path_length)
        text_file.close()
    print("Done!")


if __name__=="__main__":
    
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    f1 = 'file1'
    f2 = 'file2'
    density1 = 0.20
    alpha_freq = (8,13)
    
    task_2_7(file1, density1, alpha_freq,f1)
    task_2_7(file2, density1, alpha_freq,f2)