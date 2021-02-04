import discord
from discord.ext import commands
from random import randint
import time
import asyncio

# Variables
global logDic
messages = totalBoops = 0
listBops = ['Bop ~', 'Blep', 'Boop', 'bep', 'mlem', 'BOOP']
userBops = ['boop', 'bep', 'blep', 'bop', 'blep']

#Server ID=789251106831073281
channelID = 789251106831073281

#comman prefix
client = commands.Bot(command_prefix = '!')

### Display message of startup
@client.event
async def on_ready():
    print('Bot is up.')

### Read logs/info
with open('store.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
    message = lines[0]
    messageList = message.split(' ')
    messages = int(messageList[2])
    totalBoops = int(messageList[5])
    strDic = lines[1]
    logDic = eval(strDic)


### Keeping track of logs/info
async def update_status():
    await client.wait_until_ready()
    global messages, totalBoops, logDic
    while not client.is_closed():
        try:
            with open('store.txt', 'w') as f:
                f.write(f'Total Messages: {messages} Total Boops: {totalBoops}\n')
                f.write(str(logDic))
                # messages = 0

            await asyncio.sleep(10)   # update logs every 10 seconds
        except Exception as e:
            print(e)

@client.event
async def on_message(message):
  global messages, logDic, totalBoops
  if str(message.author) != '~Boop~#4898':
    messages += 1
    if message.content == 'boops?':
        await message.channel.send(f'{str(message.author)} has booped {logDic[str(message.author)]} times!')
        pass
    elif 'boop' in message.content or 'bop' in message.content or 'bep' in message.content or 'blep' in message.content:
        await message.add_reaction('\U0001F60E')    #sunglasses
        await message.add_reaction('\U0001F1E7')    # B
        await message.add_reaction('\U0001F1F4')    # O
        await message.add_reaction('\U0001F1F5')    # P
        if str(message.author) in logDic:
            logDic[str(message.author)] += 1
        else:
            logDic.update({str(message.author): 1})
        await message.channel.send(listBops[randint(0,len(listBops))-1])
        print(logDic)
        totalBoops += 1
# Have update_status update in the background
client.loop.create_task(update_status())

client.run('NzkzNjk5NzQzMTExOTcwODM3.X-wEfA.mLHZq8ZvLONI0SvweeBtWZ_ceyk')