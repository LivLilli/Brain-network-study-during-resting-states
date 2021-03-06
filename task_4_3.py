import networkx as nx
import infomap
from PDC import PDC
from task_4_1_2 import open_file_txt
import matplotlib.pyplot as plt
import os
import pandas as pd
'''
TASK 4.3

Compare the community structure obtained by means of two different methods
(modularity-based vs information theory-based approaches).

----------

findCommunities(G)

Takes in input a networkx graph.

Returns 

    - the Infomap results about community detection;
    
    - network representation of communities.
'''


def findCommunities(G,f):

    infomapWrapper = infomap.Infomap("--directed --two-level")

    print("Building Infomap network from a NetworkX graph...")
    for e in G.edges():
        infomapWrapper.addLink(*e)

    print("Find communities with Infomap...")
    infomapWrapper.run();


    print("Found {} modules with codelength: {}".format(infomapWrapper.numTopModules(), infomapWrapper.codelength()))

    print("Result")
    print("\n#node module")
    dic_part = {}
    for node in infomapWrapper.iterTree():
        if node.isLeaf():
            print("{} {}".format(node.physicalId, node.moduleIndex()))
            dic_part[node.physicalId] = node.moduleIndex()

    set_comm = set(dic_part.values())

    pos, labels_dic = open_file_txt("data/channel_locations.txt")
    labeled_dic_part = dict(zip(list(labels_dic.values()),list(dic_part.values())))

    part_df = pd.DataFrame.from_dict(labeled_dic_part, orient='index', columns=['Community'])
    try:
        os.remove('results/task_4_3_%s'%f+'.csv')
        part_df.to_csv('results/task_4_3_%s'%f+'.csv')
    except:
        part_df.to_csv('results/task_4_3_%s'%f+'.csv')

    set_comm = set(dic_part.values())

    pos, labels_dic = open_file_txt("data/channel_locations.txt")
    size = len(set_comm)
    count = 0
    colour = ["purple", "orange", "red", "green", "white", "cyan"]
    #plt.title("Using PDC   File:%s \n" % file)
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
    f1 = 'file1'
    f2 = 'file2'
    # density 20%
    density1 = 0.20
    alpha_freq = (8, 13)

    pdc1 = PDC(file1, alpha_freq)
    pdc2 = PDC(file2, alpha_freq)
    matrix1  = pdc1.adj_matrix(density1)
    matrix2 = pdc2.adj_matrix(density1)
    G1 = nx.from_numpy_matrix(matrix1, create_using=nx.DiGraph)
    G2 = nx.from_numpy_matrix(matrix2, create_using=nx.DiGraph)

    plt.title("Using PDC   File:%s \n" % file1)
    findCommunities(G1,f1)
    plt.show()

    plt.title("Using PDC   File:%s \n" % file1)
    findCommunities(G2,f2)
    plt.show()






