# import libraries
import numpy as np
import mne
import pandas as pd
import os

# read edf files
edf1 = mne.io.read_raw_edf('files/S003/S003R01.edf')
edf2 = mne.io.read_raw_edf('files/S003/S003R02.edf')

# join respect to ';'
header1 = ','.join(edf1.ch_names)
header2 = ','.join(edf2.ch_names)


#drop existing csv file
os.remove('S003R01.csv')
os.remove('S003R02.csv')

# save csv file
np.savetxt('S003R01.csv', edf1.get_data().T, delimiter=',', header=header1)
np.savetxt('S003R02.csv', edf2.get_data().T, delimiter=',', header=header2)

df1 = pd.read_csv('S003R01.csv', sep=',')
df2 = pd.read_csv('S003R02.csv', sep=',')

