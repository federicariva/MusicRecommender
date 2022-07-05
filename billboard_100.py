#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Function to create a dataframe with the 100 hot songs from billboard
def create_song_dataframe ():
    
    #Importing necessary libraries
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    from tqdm.notebook import tqdm
        
    # get the website url
    url = 'https://www.billboard.com/charts/hot-100'
    
    #run request on url
    response = requests.get(url, headers = {"Accept-Language" : "en-US"}) 
    
    #parse the html as soup
    soup = BeautifulSoup(response.content,'html.parser') 
    
    #get the number of songs
    len_songs = len(soup.select('h3.c-title.a-no-trucate'))
    
    #create empty lists to store song titles and song authors
    song_title = []
    song_auth = []
    rank_position = []
    
    for i in tqdm(range(len_songs)): 
        rank_position.append(i+1)
        song_title.append(soup.select('h3.c-title.a-no-trucate')[i].get_text(strip = True))
        song_auth.append(soup.select('span.c-label.a-no-trucate')[i].get_text(strip = True))
    
    # Clean and create a dataframe with this info
    song_100 = pd.DataFrame({'position': rank_position,
                             'title':song_title,
                             'author':song_auth})
    song_100 = song_100.applymap(lambda s:s.lower() if type(s) == str else s)
    return (song_100)




