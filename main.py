import discord
from discord.ext import commands
import youtube_dl
import os
import requests
import json
from keep_alive import keep_alive

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='sir ',intents=intents)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return


@bot.command(name='speak', help='Tells the bot to speak')
async def speak(ctx):
  if ctx.message.content.startswith('sir speak'):
        await ctx.message.channel.send('Hello M8!')
        return

@bot.command(name='goodboi', help='Reward the bot for a good job')
async def goodboi(ctx):
  if ctx.message.content.startswith('sir goodboi'):
        await ctx.message.channel.send('*Pat Pat*')
        return

@bot.command(name='inspire', help='Tells the bot to send an inspirational quote')
async def inspire(ctx):
  if ctx.message.content.startswith('sir inspire'):
        await ctx.channel.send(get_quote())
        return

@bot.command(name='celebrate', help='Tells the bot to celebrate')
async def celebrate(ctx):
  if ctx.message.content.startswith('sir celebrate'):
        await ctx.message.channel.send('wip')
        return



@bot.command(name='news', help='Tells the bot to give you update on his changes')
async def news(ctx):
  if ctx.message.content.startswith('sir news'):
        await ctx.message.channel.send('Born on 4/1/2021, got a few cmds, but lookin to add memes soon. type [sir help] for the current command list.')
        return



keep_alive()
bot.run(os.getenv('TOKEN'))