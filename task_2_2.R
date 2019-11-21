library(igraph)
library(qgraph)


'It extracts the adjacency matrix from the csv file created on python.

It creates a directed graph starting from the matrix.

It computes the small wordness, taking as input the graph object.'


matrix_1 = as.matrix(read.table("data/matrix1.csv", sep=","))

graph_1 = graph_from_adjacency_matrix(matrix_1,mode = "directed")

sw_1 = smallworldness(graph_1)


matrix_2 = as.matrix(read.table("data/matrix2.csv", sep=","))

graph_2 = graph_from_adjacency_matrix(matrix_2,mode = "directed")

sw_2 = smallworldness(graph_2)


'print("The Small Worldness of S003R01.edf file is",sw_1)
print("The Small Worldness of S003R02.edf file is",sw_2)'

