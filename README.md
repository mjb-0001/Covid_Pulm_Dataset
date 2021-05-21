# Semantic-Inference-Corpus 
## Uses the CORD-19 dataset and scraped data from PubMed regarding Pulmonary research papers.


The directory "word_clusters_cosine_similarity" contain 2 pickle files and a python file to read the pickle files. The file "DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS.pkl" contains a python dictionary where the keys are a covid word cluster & the values are 20 most similar pulmonary clusters. The "DICT_PULMONARY_CLUSTER_TO_COVID_20_CLUSTERS.pkl" does the same but in reverse (i.e. pulmonary cluster to 20 covid clusters)



Each cluster for both the keys and values contain 11 words with the first being the main word from which the cluster originates from.














