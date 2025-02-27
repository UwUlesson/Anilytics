import requests
import pandas as pd
import numpy as np
import getData

myHeaders = getData.headers
url = "https://api.myanimelist.net/v2/anime/52991"
myParams = {
    "fields" : "rank,popularity,num_list_users,num_scoring_users,"
}

#example
"""
{
id,title,main_picture,alternative_titles,
start_date,end_date,synopsis,mean,rank,popularity,
num_list_users,num_scoring_users,nsfw,created_at,
updated_at,media_type,status,genres,my_list_status,
num_episodes,start_season,broadcast,source,
average_episode_duration,rating,pictures,background,
related_anime,related_manga,recommendations,
studios,statistics
}
"""

response = requests.get(url,headers=myHeaders,params=myParams)
data = response.json()
print(data)

animeData = []
