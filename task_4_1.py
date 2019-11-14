#!/usr/bin/env python

import networkx as nx
from PDC import PDC
import community
'''
Determine number and composition (i.e. list of nodes) of the communities
obtained applying one of the algorithms introduced during the course.
'''

def task_4_1(file, freq):
    pdc = PDC(file, freq)
    weighted_matrix  = pdc.final_pdc_matrix()
    G = nx.from_numpy_matrix(weighted_matrix)
    ### USING NETWORKX
    # PROBLEM: it accepts just undirected graphs
    
    # dictionary: for each node the corresponding community
    # best_partition: compute the partition of the graph nodes which maximises the modularity using the Louvain heuristices
    comm_dic = dict(community.best_partition(G))
    # communieties found
    values = set(list(comm_dic.values()))
    
    print('Using: PDC    File:%s \n' % file, 'Number of communities: ', len(values))
    print('Communities Composition: ',comm_dic)
    print('\n \n')

file1 = 'data/S003R01.edf'
file2 = 'data/S003R02.edf'
# density 20%
density1 = 0.20
alpha_freq = (8, 13)

task_4_1(file1,alpha_freq)
task_4_1(file2,alpha_freq)
'''
### USING INFOMAP
infomapWrapper = infomap.Infomap("--two-level")

print("Building Infomap network from a NetworkX graph...")
for e in G.edges():
    infomapWrapper.addLink(*e)

print("Find communities with Infomap...")
infomapWrapper.run();


print("Result")
print("\n#node module")
for node in infomapWrapper.iterTree():
  if node.isLeaf():
    print("{} {}".format(node.physicalId, node.moduleIndex()))
'''