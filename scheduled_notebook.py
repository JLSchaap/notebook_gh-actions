#!/usr/bin/env python
# coding: utf-8

# This function creates the requirements.txt for a conda environment. (install pip within your conda env)

# In[ ]:


# conda env export > environment.yml


# Brief script that scrapes a website, structures the data in a DF and exports this DF to a csv file.

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# Scrape
url_datasets = "https://www.pdok.nl/datasets"

response = requests.get(url_datasets)
soup = BeautifulSoup(response.content, 'html.parser')
datasetListUnstructured = soup.find_all("article")


# In[ ]:


# Schrijf de gevonden datasets op een gestructureerde manier weg

# loop over de gevonden data
titel_list = []
categorie_list = []
link_list = []

for i in datasetListUnstructured:
    titel_list.append(i.a.text)
    categorie_list.append(i.p.text)
    link_list.append(i.a['href'])   
    
datasets = pd.DataFrame({
    "titel": titel_list,
    "categorie": categorie_list,
    "link": link_list
})


# In[ ]:


datasets.to_csv('exports/pdokWebsiteDatasets.csv', header=True)

