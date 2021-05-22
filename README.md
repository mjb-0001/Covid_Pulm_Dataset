# Semantic-Inference-Corpus 
## Uses the CORD-19 dataset and scraped data from PubMed regarding Pulmonary research papers.


The directories "word_clusters_cosine_similarity" & "word_clusters_cosine_distance" contain 2 pickle files and a python file to read the pickle files. The files "DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS.pkl" & "DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS.pkl_COSINE_DISTANCE.pkl" contain a python dictionary where the keys are a covid word cluster & the values are 20 most similar pulmonary clusters. The "DICT_PULMONARY_CLUSTER_TO_COVID_20_CLUSTERS.pkl" & "DICT_PULMONARY_CLUSTER_TO_COVID_20_CLUSTERS_COSINE_DISTANCE.pkl" do the same but in reverse (i.e. pulmonary cluster to 20 covid clusters)



Each cluster for both the keys and values contain 11 words with the first being the main word from which the cluster originates from.














