from PDC import PDC
import networkx as nx
import csv

eeg1_file = 'data/S003R01.edf'
eeg2_file = 'data/S003R02.edf'

alpha_freq = (8, 13)
density = 0.10

pdc = PDC(eeg1_file, alpha_freq)
adj_matrix = pdc.adj_matrix(density)
G = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)

with open('data/network_for_mfinder.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for v1, v2 in G.edges:
        tsv_writer.writerow([v1, v2, '1'])

# The analysis performed with mfinder can be found in data/network_motif_20000.txt
# Command to launch in the prompt:
# mfinder1.2.exe network_for_mfinder.tsv -s 3 -r 20000 -f network_motif_20000.txt
