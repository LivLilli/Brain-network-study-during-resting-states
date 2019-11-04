# Brain network study during resting states


<div align = "center"><img src="https://i2.wp.com/neurosciencenews.com/files/2017/11/mind-consciouness-neurosciencenews.jpg?fit=1400%2C933&ssl=1"></div>





>## Aim


Goal of this project is to analyze two datasets of EEG data and to prepare a report on their comparison.
EEG data are recorded from 64 electrodes with subject at rest in (i) eyes-open and (ii) eyes-closed conditions, respectively.
Analyses will span the following topics:

1) connectivity graphs

2) graph theory indices

3) motif analysis

4) community detection


Details on mandatory and optional analyses are provided below.


>## Dataset

The EEG data are available from (<a href="https://physionet.org/content/eegmmidb/1.0.0/">PhysioNet, “EEG Motor Movement/Imagery Dataset”</a>). The whole dataset contains data acquired from 109 subjects, each containing 14 runs (files) of acquisition. Only the first two runs (SxxxR01 and SxxxR02) are relevant for this project: R01 is recorded during eyes-open (EO) resting state; R02 is recorded during eyes-closed (EC) resting state.


Select the subject according to the group you belong to (our subject will be the <b>S003</b> one). 
Data is provided in EDF files (European Data Format). This format includes metadata, among which the sampling frequency and the channel labels. Several tools to read this format are freely available. For instance, a Python package can be found on <a href="https://github.com/holgern/pyedflib/blob/master/demo/readEDFFile.py">Github</a>, a Matlab mfile on <a href="https://it.mathworks.com/matlabcentral/fileexchange/31900-edfread">MatlabCentral</a>, an R package on <a href="https://cran.r-project.org/web/packages/edfReader/">CRAN </a>(untested). As last option, if you cannot find a suitable tool for the programming language you chose you can use the <a href ="https://archive.physionet.org/cgi-bin/atm/ATM">PhysiobankATM utility</a> to export data in text (CSV) format.
