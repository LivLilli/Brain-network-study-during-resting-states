from PDC import PDC

'''
TASK 1.1

Estimate functional brain connectivity among 64 channels using one of the MVAR estimators: 
Partial Directed Coherence (PDC), Direct Transfer Function (DTF). 
Select one relevant frequency value. 
Apply a threshold so that the resulting binary connectivity matrices have network density equal to 20%. 
Create a graphical representation of the binary adjacency matrix.
'''

if __name__=="__main__":
    ### TASK 1.1
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # density 20%
    density1 = 0.20
    # Alpha rythm
    alpha_freq = (8, 13)
    # initialize PDC class for file1
    pdc1 = PDC(file1, alpha_freq)
    # heatmap file 1
    pdc1.binary_heatmap(density1,'c')
    # initialize PDC class for file2
    pdc2 = PDC(file2, alpha_freq)
    # heatmap file 2
    pdc2.binary_heatmap(density1,'c')
    
