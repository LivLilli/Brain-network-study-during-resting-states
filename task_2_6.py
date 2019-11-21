from task_2_13 import task_2_1



'''
TASK 2.6

Compare the networks obtained with the analysis 1.6 in terms of graph indices.
(the choice of this task is advised only in the case of selection of task 1.6).
'''


if __name__=="__main__":
    # file name
    file1 = 'data/S003R01.edf'
    file2 = 'data/S003R02.edf'
    # density 20%
    density1 = 0.20
    # theta rythm
    theta_range = (4,7)
    
    
    task_2_1(file1, density1, theta_range)
    task_2_1(file2, density1, theta_range)
    
    
