#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import infomap
from PDC import PDC





file1 = 'data/S003R01.edf'
file2 = 'data/S003R02.edf'
# density 20%
density1 = 0.20
alpha_freq = (8, 13)

pdc = PDC(file1, alpha_freq)
weighted_matrix  = pdc.final_pdc_matrix()
G = nx.from_numpy_matrix(weighted_matrix)

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