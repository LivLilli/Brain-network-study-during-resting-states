import louvain
import igraph as ig
from PDC import PDC
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
TASK 4.1

Determine number and composition (i.e. list of nodes) of the communities
obtained applying one of the algorithms introduced during the course.
'''


'''
task_4_1(file, freq, density)

It takes in inputs:

    * edf file name;
    
    * frequency range;
    
    * density value.
    
It applies the Louvain Algo to Directed Graph.


Returns:

    * a dictionary (for each node, the corresponding community);
    
    * list of community names, without duplicates.
'''
def task_4_1(file, freq, density) :
    pdc = PDC(file, freq)
    matrix = pdc.adj_matrix(density)
    G = ig.Graph.Adjacency(list(matrix), mode="directed")
    part = louvain.find_partition(G, louvain.ModularityVertexPartition)

    keys = list(range(0, len(part)))
    # values = list of list
    # each i-sublist has nodes i-community
    values = []
    for i in range(len(keys)) :
        values.append(part[i])

    # list of keys of our future dictionary
    ll = []
    for key in keys :
        for i in range(len(values[key])) :
            # list of zeros
            ll.append(key)
    # list of all the values of future dictionary
    vv = []
    for i in range(len(values)):
        vv += values[i]
    # dictionary
    communities_dic = dict(zip(vv, ll))

    return communities_dic, keys


'''
TASK 4.2

Make a graphical representation of the community structure in both rest conditions.
'''

'''
open_file_txt(file)

Takes in input the txt file name.


It extract coordinates values from given txt file.
Returns:

    * dictionary of coordinates (for each node, tuple of coords);
    
    * dictionary of labels (for each node, corresponding channel name).

'''
def open_file_txt(file) :
    # delimiter: multiple spaces
    table = pd.read_csv(file, delimiter='\s+')
    # list of x coord
    coord_x = list(table.x)
    # list of y coord
    coord_y = list(table.y)
    # list of labels
    labels_list = list(table.label)
    for i in range(len(coord_x)) :
        # clean labels name
        labels_list[i] = labels_list[i].replace('..', '')
        labels_list[i] = labels_list[i].replace('.', '')
    # list of coord tuple (x,y)
    coord_list = []
    for x, y in zip(coord_x, coord_y) :
        coord_list.append((x, y))
    # list of indexes from 0 to 64
    indexes = list(range(0, len(coord_x)))
    # dictionary of coordinates
    # keys from 0 to 64
    coord_dic = dict(zip(indexes, coord_list))
    # dictionary of labels
    nodes = np.arange(0, len(coord_dic))
    labels_dic = dict(zip(nodes, labels_list))

    return coord_dic, labels_dic
'''
task_4_2(set_comm, dic_part, file, freq)

Takes in input:

    * ordered list of communities names (0,1,2..), no duplicates
    
    * dictionary of communites (for each node, corresponding communities
    
    * edf file name
    
    * frequency range
'''

def task_4_2(set_comm, dic_part, file, freq) :
    pdc = PDC(file, freq)
    weighted_matrix = pdc.final_pdc_matrix()
    G = nx.from_numpy_matrix(weighted_matrix)
    pos, labels_dic = open_file_txt("data/channel_locations.txt")
    size = len(set_comm)
    count = 0
    colour = ["purple", "orange", "red", "green", "white", "cyan"]
    plt.title("Using PDC   File:%s \n" % file)
    for com in set_comm :
        count = count + 1
        list_nodes = [nodes for nodes in dic_part.keys()
                      if dic_part[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20,
                               node_color=colour[com])

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()

if __name__=="__main__":

    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    alpha_freq = (8, 13)
    density = 0.20

    ### task 4.1

    dic_part_1, set_comm_1= task_4_1(file1, alpha_freq, density)
    dic_part_2, set_comm_2 = task_4_1(file2, alpha_freq, density)



    ### task 4.2
    task_4_2(set_comm_1,dic_part_1,file1,alpha_freq)
    task_4_2(set_comm_2,dic_part_2,file2,alpha_freq)
