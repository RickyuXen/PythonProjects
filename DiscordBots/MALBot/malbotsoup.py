import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import requests

global topair, topup
# WEB SCRAPING W/ SOUP:
@tasks.loop(seconds=60.0)
async def checkTop():
    global topair, topup
    topair = []
    topup = []
    source = requests.get('https://myanimelist.net/').text
    soup = BeautifulSoup(source, 'lxml')
    TopAiring = soup.find('div', class_='widget airing_ranking right')
    topUpcomming = soup.find('div', class_='widget upcoming_ranking right')
    
    for TopAnime in TopAiring.find_all('li', class_='ranking-unit'):
        for a in TopAnime.p.find_all('a', href=True):
            topair.append(a['href'])

    for Upcomming in topUpcomming.find_all('li', class_='ranking-unit'):
        for a in Upcomming.p.find_all('a', href=True):
            topup.append(a['href'])

checkTop.start()

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('MAL bot is online.')

@client.event
async def on_message(message):
    global topair, topup
    if message.content == ".topair":
        await message.channel.send(f'The current top airing anime are:')
        for num in range(1, len(topair)+1):
            await message.channel.send(f'{num}. {topair[num-1]}')
            
    if message.content == '.topup':
        await message.channel.send(f'The current upcomming anime are:')
        for num in range(1, len(topup)+1):
            await message.channel.send(f'{num}. {topup[num-1]}')
    
for num in range(1, len(topair)+1):
    print(f'{num}. {topair[num-1]}')
# @client.command()
# async def test(ctx):

#change key
client.run()