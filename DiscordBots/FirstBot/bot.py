import discord
from discord.ext import commands
from random import randint
import time
import asyncio

# Variables
messages = joined = messageDelete = 0

#Server ID=789251106831073281
channelID = 789251106831073281

#comman prefix
client = commands.Bot(command_prefix = '/')

### Display message of startup
@client.event
async def on_ready():
    print('Bot is up.')

### Keeping track of logs/info
async def update_status():
  await client.wait_until_ready()
  global messages, joined, messageDelete

  while not client.is_closed():
    try:
      with open('stats.txt', 'a') as f:
        f.write(f'Time: {int(time.time())}; messages: {messages}; Members Joined: {joined}; Messages deleted: {messageDelete}\n')

        messages = 0
        joined = 0
        messageDelete = 0

      await asyncio.sleep(3600)
    except Exception as e:
      print(e)


# Client events;
@client.event
async def on_member_join(member):
  global joined
  joined += 1
  await channel.purge(limit=1)
  await channel.send(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
  for channel in member.guild.channels:
    if str(channel) == "greetings":
      await channel.send(f'Goodbye {member}')
      print(f'{member} has swished out :(')

@client.event
async def on_message(message):
  global messages
  messages += 1
  await client.process_commands(message)
  id = client.get_guild(789251106831073281)
  channels = ["commands"]
  valid_users =['RickyuXen#3176', 'RandoBot#0844', 'Stressed by a Mountain of Books#4462']
  valid_commands = ['.hello', '.boop', '.users']

  print(message.content)

  if str(message.channel) in channels and str(message.author) in valid_users:   ## Works only in list of channels above
    if message.content.find('.hello') != -1:
      await message.channel.send(f'wassupp {message.author.mention}!')
    if message.content.find('.boop') != -1:
      await message.channel.send('Bop!')
    if message.content == '.users':
      await message.channel.send(f'Total number of members: {id.member_count}')
  elif str(message.channel) not in channels and str(message.content) in valid_commands:
    await message.channel.send(f'{message.content} can only be used in valid channels;')
    print(f'{message.author} tried to use command {message.content} in {message.channel}')
  if str(message.author) != 'RandoBot#0844':
    if message.content.find('league') != -1:
      await message.channel.send(f'{message.author} is talking about league! Go harrass \'em! @everyone')
  
  # if 'boop' in message.content or 'bop' in message.content or 'bep' in message.content:
  if str(message.author) != 'RandoBot#0844':
    if 'boop' in message.content or 'bop' in message.content or 'bep' in message.content:
        await message.channel.send('Bop ~')
    if message.content == 'boops?':
        await message.channel.send(f'{str(message.author)} has booped many times!')

### Commands
# with / command ; doesn't work; when on_message exists and there have been no check on the process of commands
# respond command; simply returns the string inputted
@client.command()
async def respond(ctx, *arg):
  completeString = ''
  if arg == ():
    await ctx.send('No arguments')
  else:
    for eachstring in arg:
      completeString += (str(eachstring) + ' ')
    await ctx.send(completeString)

# harass command; (@name, #of times)
@client.command()
async def harass(ctx, *arg):
  harassList = ['sucks ass', 'is quite dumb', 'is extremely dumb', 'cannot be me, lmfao','can suck deez nutz', 'has an IQ lower than a newborn infant', 'is quite cringe', 'is a monke', 'failed kindergarten', 'has a small brain', 'has an underdeveloped brain']
  member = arg[0]
  times = int(arg[1])
  check = 0
  while check <= times:
    check +=1
    randNum = randint(0, len(harassList)-1)
    await ctx.send(f'{member} {harassList[randNum]}')

@client.command()
async def harassonce(ctx, *arg):
  harassList = ['sucks ass', 'is quite dumb', 'is extremely dumb', 'cannot be me, lmfao','can suck deez nutz', 'has an IQ lower than a newborn infant', 'is quite cringe', 'is a monke', 'failed kindergarten', 'has a small brain', 'has an underdeveloped brain']
  member = arg[0]
  times = int(arg[1])
  check = 0
  string = ''
  try:
    while check <= times:
      check +=1
      randNum = randint(0, len(harassList)-1)
      string += f'{member} {harassList[randNum]}\n'
    await ctx.send(string)
  except Exception as e:
    await ctx.send('Max lines avaiable to send: 47\n"/harass @name #of times"')

# deletes previous messages
@client.command()
async def delete(ctx, arg):
  global messageDelete
  messageDelete += int(arg)
  await ctx.channel.purge(limit=int(arg)+1)
  await ctx.channel.send(f'Removing {arg} messages...')

# Have update_status update in the background
client.loop.create_task(update_status())

client.run('NzkwNDIyNTU4NjMzMjMwMzc3.X-AYXw.SkFnBThN_4dHXJWSxoNqSYEMWJQ')