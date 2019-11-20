import louvain
import igraph as ig
from PDC import PDC


if __name__=="__main__":

    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    alpha_freq = (8, 13)
    density = 0.20
    pdc = PDC(file1, alpha_freq)
    matrix1 = pdc.adj_matrix(density)
    G1 = ig.Graph.Adjacency(list(matrix1),mode="directed")
    part = louvain.find_partition(G1, louvain.ModularityVertexPartition)
    print(part)
    # crea dizionario con chiavi 0,1...
    # e valori part[0], ..