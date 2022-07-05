#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hot_song():
    
    from billboard_100 import create_song_dataframe # get the dataframe of 100 hotsong in billboard
    print ('loading data...')
    song_100 = create_song_dataframe()
    
    #get the input from the user
    song = input('Would you like a song recommendation? Please write here the title of a song you like!').lower()
    
    if len(song) < 2:
        print('This doesn not look like the title of a song. Please try again!')
    elif song in song_100['title'].tolist():
        print("Your song is in the top 100!")
        index = song_100.index[song_100['title'] == song].tolist()
        song_100_temp = song_100.drop(song_100.index[index])
        recomen = song_100_temp.sample(n=1) # Randomly sample 1 element from your dataframe
        print('The recommended song for you is: ' + recomen['title'].to_string(index = False) + ' from '+ recomen['author'].to_string(index = False))
    else:
        print('I cannot find matches for this song, please try with another song!')

