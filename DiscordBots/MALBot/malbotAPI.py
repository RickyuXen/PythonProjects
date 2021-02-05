import discord
from discord.ext import commands, tasks
import json
import requests

client = commands.Bot(command_prefix = '.')

# Bot is ready
@client.event
async def on_ready():
    print('MAL bot is online.')

# TOP ANIME/MANGA
@client.command()
async def top(ctx, *arg):
    try:
        global singleString
        kind = arg[0]
        typeOf = arg[1]
        amount = arg[2]
        response = requests.get(f'https://api.jikan.moe/v3/top/{kind}/1/{typeOf}')  # request from Jikan MAL API
        jsonTop = response.json()
        top = jsonTop['top']
        for dictionary in top:
            rank = dictionary['rank']   # Assign values
            anime = dictionary['title']
            url = dictionary['url']
            image = dictionary['image_url']
            score = dictionary['score']
            if rank <= int(amount): # Send bot message with requested information
                await ctx.channel.send(f'Rank {rank}.\n{anime} | score: {score}\n{url}')
    except Exception as e:
        print(e)
        await ctx.channel.send(f'Something went wrong;\nanime: airing, upcoming, movie\nmanga: manga, novels, manhwa, manhua\nBoth: bypopulariy, favorite\nsyntax: \".top type typeof amount\"')

# token
token = open("malToken.txt", "r")

client.run(token.read())