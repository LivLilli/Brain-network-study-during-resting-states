import networkx as nx
from PDC import PDC
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

# Indicate EEG number, either R01 o R02
filenum = 'R02'
eeg_file = 'data/S003'+filenum+'.edf'
alpha_freq = (8, 13)
density = 0.10

pdc = PDC(eeg_file, alpha_freq)
adj_matrix = pdc.adj_matrix(density)
G = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)


# Instantiate new graph with same nodes as the original one
G_motif = nx.DiGraph()
G_motif.add_nodes_from(G.nodes)

# Open mfinder analysis for the particular A->B<-C motif and instantiate the incident graph
# We've used the flag osmem to get subgraph of the specific motif (id 36)
duplicates = 0
with open('data/network_'+filenum+'_mfinder_dens10_id36_MEMBERS.txt') as motif_file:
    csv_reader = csv.reader(motif_file, delimiter='\t')
    for v1, v2, v3 in csv_reader:
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        if not G_motif.has_edge(v1, v3):
            G_motif.add_edge(v1, v3)
        else:
            duplicates += 1
        if not G_motif.has_edge(v2, v3):
            G_motif.add_edge(v2, v3)
        else:
            duplicates += 1

# Printing some stats
print(str(duplicates) + " duplicates found")
print("Length of G: " + str(len(G.nodes)))
print("Length of G_motif: " + str(len(G_motif.nodes)))

#Plot the resulting graph
cl = pd.read_csv("data/channel_locations.txt", delimiter= '\s+')
coord_x = list(cl.x)
coord_y = list(cl.y)
labels_list = list(cl.label)
for i in range(len(coord_x)):
    labels_list[i] = labels_list[i].replace('..', '')
    labels_list[i] = labels_list[i].replace('.', '')
coord_list = []
for x,y in zip(coord_x, coord_y):
    coord_list.append((x, y))
indexes = list(range(0, len(coord_x)))
coord_dic = dict(zip(indexes, coord_list))
nodes = np.arange(0,len(G_motif.nodes))
channel_names = labels_list
labels_dic = dict(zip(nodes, channel_names))

plt.figure(num=None, figsize=(20, 16), dpi=160, facecolor='w', edgecolor='k')
plt.title(r'Connection involving $A \rightarrow B \leftarrow C$ motif in file $S003'+filenum+'.edf$', fontsize='x-large')
nx.draw_networkx_nodes(G_motif, pos=coord_dic)
nx.draw_networkx_edges(G_motif, pos=coord_dic, arrowstyle='->', width=0.5)
nx.draw_networkx(G_motif, pos=coord_dic, labels=labels_dic, nodelist=list(labels_dic.keys()), node_size=750)
plt.savefig('data/'+filenum+'_motif_id36.png')
plt.show()

# Task 3.3

# For the analysis we've chosen electrode Po4

# For each motif determine whether node Po4 (58) is involved or not
motif_graphs = {}
# Change folder
os.chdir('data/subgraph_motif/'+filenum)
for motif_file_path in os.listdir(os.getcwd()):
    with open(motif_file_path) as motif_file:
        G_motif_spec = nx.DiGraph()
        G_motif_spec.add_nodes_from(G.nodes)
        csv_reader = csv.reader(motif_file, delimiter='\t')
        for v1, v2, v3 in csv_reader:
            v1 = int(v1)
            v2 = int(v2)
            v3 = int(v3)
            if not G_motif_spec.has_edge(v1, v3):
                G_motif_spec.add_edge(v1, v3)
            if not G_motif_spec.has_edge(v2, v3):
                G_motif_spec.add_edge(v2, v3)
        motif_graphs[motif_file.name] = G_motif_spec

po4_num = 58
po4_involve = []

for file_motif, graph in motif_graphs.items():
    if graph.in_edges(po4_num) or graph.edges(po4_num):
        po4_involve.append(file_motif)

print("Regardug "+filenum+" List of all 3-nodes motif in which node Po4 is involved, the motif could be recover from the id:")
print(po4_involve)
print("Number of motifs in wich Po4 is involved")
print(len(po4_involve))


