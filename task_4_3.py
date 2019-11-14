import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import infomap
from PDC import PDC


'''
Compare the community structure obtained by means of two different methods
(modularity-based vs information theory-based approaches).

'''


file1 = 'data/S003R01.edf'
file2 = 'data/S003R02.edf'
# density 20%
density1 = 0.20
alpha_freq = (8, 13)

pdc1 = PDC(file1, alpha_freq)
weighted_matrix1  = pdc1.final_pdc_matrix()
G1 = nx.from_numpy_matrix(weighted_matrix1, create_using=nx.DiGraph)
pdc2 = PDC(file2, alpha_freq)
weighted_matrix2  = pdc2.final_pdc_matrix()
G2= nx.from_numpy_matrix(weighted_matrix2, create_using=nx.DiGraph)
def findCommunities(G):

    infomapWrapper = infomap.Infomap("--two-level")

    print("Building Infomap network from a NetworkX graph...")
    for e in G.edges():
        infomapWrapper.addLink(*e)

    print("Find communities with Infomap...")
    infomapWrapper.run();

    print("Found {} modules with codelength: {}".format(infomapWrapper.numTopModules(), infomapWrapper.codelength()))

    print("Result")
    print("\n#node module")
    for node in infomapWrapper.iterTree():
        if node.isLeaf():
            print("{} {}".format(node.physicalId, node.moduleIndex()))
findCommunities(G2)