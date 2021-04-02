import discord
from discord.ext import commands,tasks
import os
import requests
import json
import youtube_dl
import asyncio
from discord.utils import get
from discord import FFmpegPCMAudio
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









youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '172.18.0.1' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename
        

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


        
@bot.command(name='play', help='To play song')
async def play(ctx,url):
    try :
        voice = get(bot.voice_clients, guild=ctx.guild)

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

keep_alive()
bot.run(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))