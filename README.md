# Semantic-Inference Corpus
## Uses the CORD-19 dataset and scraped data from PubMed regarding Pulmonary research papers.


Both directories contain 2 pickle files which contain python dictionaries. The keys of the dictionary correspond do a singular covid/pulm cluster (depending on the file). The matching values for a key are the 20 most similar covid/pulm clusters.

* Files w/ covid keys 
	* DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS_COSINE_SIM.pkl
	* DICT_COVID_CLUSTER_TO_PULMONARY_20_CLUSTERS_COSINE_DISTANCE.pkl
* Files w/ pulm keys
	* DICT_PULM_CLUSTER_TO_COVID_20_CLUSTERS_COSINE_SIM.pkl
	* DICT_PULM_CLUSTER_TO_COVID_20_CLUSTERS_COSINE_DISTANCE.pkl  
	
	
<br > <br >
Each directory also contains a python file to aid in reading the pkl files. 



