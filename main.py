import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/sir speak'):
        await message.channel.send('Hello M8!')

    if message.content.startswith('/sir goodboi'):
        await message.channel.send('Ty!')

    if message.content.startswith('/sir slur'):
        await message.channel.send('FuCk!')

    if message.content.startswith('/sir is brian gay?'):
        await message.channel.send('Yes')

client.run(os.getenv('TOKEN'))