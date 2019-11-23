# import class
from PDC import PDC
'''
TASK 1.3

Perform task 1.1 using thresholds yielding the following density values:

1%, 5%, 10%, 20%, 30%, 50%.
'''

if __name__=="__main__":
    ### TASK 1.1
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # alpha rythm
    alpha_freq = (8,13)
    # initialize PDC class for file1
    pdc1 = PDC(file1, alpha_freq)
    # initialize PDC class for file2
    pdc2 = PDC(file2, alpha_freq)
    # density 1%
    density2 = 0.01
    pdc1.binary_heatmap(density2,'w')
    pdc2.binary_heatmap(density2, 'w')
    # density 5%
    density3 = 0.05
    pdc1.binary_heatmap(density3, 'b')
    pdc2.binary_heatmap(density3,'b')
    # density 10%
    density4 = 0.10
    pdc1.binary_heatmap(density4,'g')
    pdc2.binary_heatmap(density4,'g')
    # density 30%
    density5 = 0.30
    pdc1.binary_heatmap(density5, 'r')
    pdc2.binary_heatmap(density5, 'r')
    # density 50%
    density6 = 0.50
    pdc1.binary_heatmap(density6,'#ffc0cb')
    pdc2.binary_heatmap(density6, '#ffc0cb')