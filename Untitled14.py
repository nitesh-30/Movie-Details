#!/usr/bin/env python
# coding: utf-8

# In[11]:


import csv


# In[1]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


# In[2]:


headers = {"Accept-Language": "en-US,en;q=0.5"}


# In[3]:


movie_name = []
year = []
time=[]
rating=[]
metascore =[]
votes = []
gross = []
description = []


# In[4]:


pages = np.arange(1,1000,100)


# In[5]:


for page in pages:
    page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(page)+"&ref_=adv_nxt")
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})
    sleep(randint(2,8))
    for store in movie_data:
        name = store.h3.a.text
        movie_name.append(name)
        
        year_of_release = store.h3.find('span', class_ = "lister-item-year text-muted unbold").text
        year.append(year_of_release)
        
        runtime = store.p.find("span", class_ = 'runtime').text
        time.append(runtime)
        
        rate = store.find('div', class_ = "inline-block ratings-imdb-rating").text.replace('\n', '')
        rating.append(rate)
        
        meta = store.find('span', class_ = "metascore").text if store.find('span', class_ = "metascore") else "****"
        metascore.append(meta)
        
        
        value = store.find_all('span', attrs = {'name': "nv"})
        
        vote = value[0].text
        votes.append(vote)
        
        grosses = value[1].text if len(value)>1 else '%^%^%^'
        gross.append(grosses)
       
        


# In[8]:


movie_list = pd.DataFrame({ "Movie Name": movie_name, "Year of Release" : year, "Watch Time": time,"Movie Rating": rating, "Meatscore of movie": metascore, "Votes" : votes, "Gross": gross })


# In[9]:


movie_list


# In[13]:


movie_list.to_excel("Detail of 1000 movie.xlsx")


# In[ ]:




