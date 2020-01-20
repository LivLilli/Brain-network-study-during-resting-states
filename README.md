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


>## Tasks


>### 1. Connectivity graph

1.1. (mandatory) Estimate functional brain connectivity among 64 channels using one of the MVAR estimators: Partial Directed Coherence (PDC), Direct Transfer Function (DTF). Select one relevant frequency value. Apply a threshold so that the resulting binary connectivity matrices have network density equal to 20%. Create a graphical representation of the binary adjacency matrix.


1.2. (class ‘A’) Perform task 1.1 using both estimators (PDC and DTF).


1.3. (class ‘A’) Perform task 1.1 using thresholds yielding the following density values: 1%, 5%,
10%, 20%, 30%, 50%.


1.4. (class ‘D’) Considering the subset of 19 channels suggested in Figure 1 and Table 2, estimate
the connectivity using PDC or DTF and apply a statistical validation method (asymptotic statistics7, resampling procedure8,...) to filter out values that are not significantly different from 0 (𝑃𝐷𝐶(𝑖, 𝑗) ≠ 0 𝑤𝑖𝑡h 𝑝 < 5%).


1.5. (class ‘C’) Make a topographical representation of the networks (see example in Figure 2). Cartesian coordinates of planar representation of EEG channels are available in Table 3 (see
also the file channel_locations.txt). (the choice of this task is advised in the case of 19-channel networks and/or density≤5%).
 
 
1.6. (class ‘B’) Perform task 1.1 considering a second frequency value belonging to a different EEG rhythm with respect to the first choice.


>### 2. Graph theory indices

2.1. (mandatory) Compute binary global (clustering coefficient, path length) and local (degree,
in/out-degree) graph indices. List the highest 10 channels for local indices.


2.2. (class ‘D’) Search in the literature a definition of small-worldness index (i.e. an index
describing the small-world organization of a network) and compute it.


2.3. (class ‘B’) Compare the global indices extracted from PDC and DTF connectivity estimations.


2.4. (class ‘C’) Study the behaviour of global graph indices in function of network density (see
point 2.3 for density values).
(the choice of this task is advised in the case of selection of task 1.3).


2.5. (class ‘B’) Make a topographical representation of local indices.


2.6. (class ‘B’) Compare the networks obtained with the analysis 1.6 in terms of graph indices.
(the choice of this task is advised only in the case of selection of task 1.6).


2.7. (class ‘C’) Perform point 2.1 considering the weighted version of the graph indices definitions.


>### 3. Motif analysis


3.1. (mandatory) Perform motifs analysis to investigate the presence of 3-node configurations in
the networks: determine their frequency and statistical significance (motifs, anti-motifs).


3.2. (class ‘C’) For the motif with pattern 𝐴 → 𝐵 ← 𝐶, create a topographical representation of the
networks considering only the connections involved in this configuration.


3.3. (class ‘C’) Choose a channel selected in parieto-occipital scalp region and determine the
motifs which involve it.


3.4. (class ‘E’) Perform the same analysis described in task 3.1 considering 4-node motifs.


>### 4. Community detection


4.1. (mandatory) Determine number and composition (i.e. list of nodes) of the communities
obtained applying one of the algorithms introduced during the course.


4.2. (class ‘B’) Make a graphical representation of the community structure in both rest conditions.


4.3. (class ‘C’) Compare the community structure obtained by means of two different methods
(modularity-based vs information theory-based approaches).

