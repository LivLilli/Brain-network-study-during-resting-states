# import libraries

import warnings
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from PDC import PDC
# Filter out warnings
warnings.filterwarnings("ignore", category=FutureWarning)

'''
TASK 1.5 

Make a topographical representation of the networks (see example in Figure 2). 

Cartesian coordinates of planar representation of EEG channels are available in Table 3 (see
also the file channel_locations.txt). 

(the choice of this task is advised in the case of 19-channel networks and/or density≤5%).
sub_PDC() class 


----------------------------------------


SubPDC()

Compute PDC on just a subset of channels.

Make a graphical representation of the network, using given Cartesian coordinates
'''


def open_file_txt(txt_name) :
    '''
    Returns:
         - dictionary of coordinates (for each node, a tuple)

         - labels list
    '''

    # delimiter: multiple spaces
    table = pd.read_csv(txt_name, delimiter='\s+')
    # list of x coord
    coord_x = list(table.x)
    # list of y coord
    coord_y = list(table.y)
    # labels
    labels = list(table.label)
    for i in range(len(labels)):
        # clean labels name
        labels[i] = labels[i].replace('..','')
        labels[i] = labels[i].replace('.','')

    # list of coord tuple (x,y)
    coord_list = []
    for x, y in zip(coord_x, coord_y) :
        coord_list.append((x, y))
    # list of indexes from 0 to 64
    indexes = list(range(0, len(coord_x)))
    # dictionary of coordinates
    # keys from 0 to 64
    coord_dic = dict(zip(indexes, coord_list))

    return coord_dic, labels

def graph(file, density, freq):
    pos_dic, labels = open_file_txt("data/channel_locations.txt")
    dic_labels = dict(zip([x for x in range(len(labels))], labels))
    pdc = PDC(file, freq)
    adj = pdc.adj_matrix(density)
    G = nx.from_numpy_matrix(adj, create_using= nx.DiGraph)
    plt.title('Using PDC \n File: %s' %file+'    Density: %f' %density)
    nx.draw_networkx(G, pos = pos_dic, labels = dic_labels, node_color = 'cyan')
    plt.show()



if __name__ == "__main__":
    ### TASK 1.5
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    txt_file = 'data/channel_locations.txt'
    # advised density 5%
    density = 0.05

    alpha = (8,13)
    graph(file1, density, alpha)
    plt.show()

    graph(file2, density, alpha)
    plt.show()













