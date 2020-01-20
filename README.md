# Brain network study during resting states


<div align = "center"><img src="https://i2.wp.com/neurosciencenews.com/files/2017/11/mind-consciouness-neurosciencenews.jpg?fit=1400%2C933&ssl=1"></div>





>## Aim

The study about interactions among hemispheres’ lobes is a main aspect of Neuroscience. Our goal was to compute an in-depth analysis and a comparison of two given datasets of EEG data (respectively related to eyes open EO and eyes closed EC resting states). In particular, we considered the corresponding networks, obtained from a Partial Directed Coherence (PDC) estimation, followed by the selection of Alpha rhythm and of a threshold in order to obtain a density of 20% (these were our default settings, unless others were specified by tasks). Our aim was to study, through graphs properties, the communications among channels, trying to find some emergent sub-structure in the brain network, communities and most involved lobes.

Analyses will span the following topics:

1) connectivity graphs

2) graph theory indices

3) motif analysis

4) community detection



>## Dataset

The EEG data are available from (<a href="https://physionet.org/content/eegmmidb/1.0.0/">PhysioNet, “EEG Motor Movement/Imagery Dataset”</a>). The whole dataset contains data acquired from 109 subjects, each containing 14 runs (files) of acquisition. Only the first two runs (SxxxR01 and SxxxR02) are relevant for this project: R01 is recorded during eyes-open (EO) resting state; R02 is recorded during eyes-closed (EC) resting state. Data is provided in EDF files (European Data Format). This format includes metadata, among which the sampling frequency and the channel labels.






