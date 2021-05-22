
#------------------------------------------------------------
#DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS_COSINE_DISTANCE.pkl
import pickle as pkl

with open('DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS_COSINE_DISTANCE.pkl', 'rb') as f:
    pickle_file_covid = pkl.load(f)
print(len(pickle_file_covid))


##This results in length 47838

#------------------------------------------------------------






#------------------------------------------------------------

#DICT_PULMONARY_CLUSTER_TO_COVID_20_CLUSTERS_COSINE_DISTANCE.pkl

import pickle as pkl

with open('DICT_PULMONARY_CLUSTER_TO_COVID_20_CLUSTERS_COSINE_DISTANCE.pkl', 'rb') as f:
    pickle_file_pulm = pkl.load(f)
print(len(pickle_file_pulm))


##This results in length 57889



#------------------------------------------------------------