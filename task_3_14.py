from PDC import PDC
import networkx as nx
import csv

eeg_file = 'data/S003R01.edf'

alpha_freq = (8, 13)
density = 0.10

pdc = PDC(eeg_file, alpha_freq)
adj_matrix = pdc.adj_matrix(density)
G = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)

with open('data/network_R01_mfinder_dens10.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for v1, v2 in G.edges:
        # Third element set to 1 because the package will ignore different values
        tsv_writer.writerow([v1, v2, '1'])

# The analysis performed with mfinder can be found in data/network_motif_20000.txt
# Command to launch in the prompt:
# mfinder1.2.exe network_for_mfinder.tsv -s 3 -r 20000 -f network_motif_20000.txt

# To perfrom 4-node motif analysis we've used a similar approach but in order to complete the analysis
# with a reasonable time we kept the random graph generator parameter at 500 instead of 20000 as it was for 3-node motif
# Command to launch in the prompt:
# mfinder1.2.exe data\network_R01_mfinder_dens10.tsv -s 4 -r 500 -f R01_dens10_size4_rand500
# The output of the analysis can be found in data/R01_dens10_size4_rand500_OUT.txt
