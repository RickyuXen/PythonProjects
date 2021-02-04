import requests
import json

page = input('TOP?:')
allowed = ['airing', 'upcoming', 'movie', 'bypopularity']

if page in allowed:
    response = requests.get(f'https://api.jikan.moe/v3/top/anime/1/{page}')
    # print(response.json())
    jsonTop = response.json()
    top = jsonTop['top']
# print(top)

# print out top airing animes
for dictionary in top:
    rank = dictionary['rank']
    anime = dictionary['title']
    url = dictionary['url']
    image = dictionary['image_url']
    score = dictionary['score']
    if rank <= 10:
        print(f'Rank {rank}. {anime} | score: {score} | {url}')
# print(jsonTop['top'])
# print(topDic)
