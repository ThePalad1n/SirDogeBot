import discord
from discord.ext import commands
import os
import requests
import json
import math
import urllib
import random
from keep_alive import keep_alive

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='sir ', intents=intents)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


#silly command
@bot.command(name='speak', help='Tells the bot to speak')
async def speak(ctx):
    if ctx.message.content.startswith('sir speak'):
        await ctx.message.channel.send('Hello M8!')
        return


#inside joke with a server memeber
@bot.command(name='barps', help='Pulls a BARPS')
async def barps(ctx):
    if ctx.message.content.startswith('sir barps'):
        await ctx.message.channel.send('NO NIKHIL!')
        return


#silly starwars meme cmd
@bot.command(name='hmp', help='unlimited power meme')
async def hmp(ctx):
    if ctx.message.content.startswith('sir hmp'):
        await ctx.message.channel.send('UNLIMITED POWER!')
        return


#sill cmd for bot reward
@bot.command(name='goodboi', help='Reward the bot for a good job')
async def goodboi(ctx):
    if ctx.message.content.startswith('sir goodboi'):
        await ctx.message.channel.send('*Pat Pat*')
        return


#inspiration command from api
@bot.command(name='inspire',
             help='Tells the bot to send an inspirational quote')
async def inspire(ctx):
    if ctx.message.content.startswith('sir inspire'):
        await ctx.channel.send(get_quote())
        return


#fun little dice roll
@bot.command(name='rolld20', help='rolls a d20 to test your luck')
async def rolld20(ctx):
    if ctx.message.content.startswith('sir rolld20'):
        await ctx.message.channel.send("Rolling D20")
        value = random.randint(1, 20)
        if (value > 19):
            await ctx.message.channel.send("AYE Nat 20 Baby!")
        elif (value > 15 and value < 20):
            await ctx.message.channel.send(
                "Hey thats pretty good you rolled a % d " % (value))
        elif (value > 10 and value < 15):
            await ctx.message.channel.send("Not bad you rolled a % d " %
                                           (value))
        elif (value > 1 and value < 10):
            await ctx.message.channel.send(
                "Oof could be better you rolled a % d " % (value))
        elif (value < 2):
            await ctx.message.channel.send("Eeeeelllllsssss Nat 1")
        else:
            await ctx.message.channel.send("Huh thats not supposed to happen")
        return


#silly meme cmd
@bot.command(name='bingbong', help='Fuck ya Life')
async def bingbong(ctx):
    if ctx.message.content.startswith('sir bingbong'):
        await ctx.message.channel.send('Fuck ya Life!')
        return


#silly work command
@bot.command(name='jillamy', help='The cult')
async def jillamy(ctx):
    if ctx.message.content.startswith('sir jillamy'):
        await ctx.message.channel.send('<a:alert:814971914086121472>' +
                                       'Go Jillamy Go!!!' +
                                       '<a:alert:814971914086121472>')
        await ctx.message.channel.send('one of us')
        await ctx.message.channel.send('One Of Us')
        await ctx.message.channel.send('ONE OF US')
        return


#magic eight ball command. could be compacted with a switch probs
@bot.command(name='magic8', help='The decision make youve always wanted')
async def magic8(ctx):
    if ctx.message.content.startswith('sir magic8'):
        value = random.randint(1, 20)
        if (value == 20):
            await ctx.message.channel.send("Certified BIG bet.")
        elif (value == 19):
            await ctx.message.channel.send("Naw but you'll get stinky feet.")
        elif (value == 18 or value == 3):
            await ctx.message.channel.send("Maybe...")
        elif (value == 17 or value == 4):
            await ctx.message.channel.send("No shot.")
        elif (value == 15 or value == 5 or value == 10):
            await ctx.message.channel.send("Try again.")
        elif (value == 16 or value == 6):
            await ctx.message.channel.send("Possible but not probable.")
        elif (value == 14 or value == 7):
            await ctx.message.channel.send(
                "Ill ask Bill Nye and get back to you.")
        elif (value == 13 or value == 8):
            await ctx.message.channel.send(
                "Don't worry about it just go play some Halo.")
        elif (value == 12 or value == 9):
            await ctx.message.channel.send("No.")
        elif (value == 11 or value == 2):
            await ctx.message.channel.send("Yes.")
        elif (value == 1):
            await ctx.message.channel.send("Never ask me a question again.")
        else:
            await ctx.message.channel.send("Wait how did you do that???")


#attempting to create a poll cmd work in progress
'''
@bot.command(help = "a cmd to create a poll.")
async def poll(ctx, *, question: str):
    if ctx.message.content.startswith('sir poll'):
      await ctx.message.channel.send("What are you polling?")
      question = ctx.message.author
      message = await ctx.send(f"{question} \nY = Yes**\n**N = No**")
      await message.add_reaction('N')
      await message.add_reaction('Y')
'''


#silly celebration command
@bot.command(name='c', help='A cmd build to celebrate')
async def c(ctx):
    if ctx.message.content.startswith('sir c'):
        await ctx.message.channel.send('C o n g r a t s!')
        await ctx.message.channel.send('<a:ye:814971851485872140>' +
                                       '<a:catjam:824878456939610112>' +
                                       '<a:beat:814971891969294396>' +
                                       '<a:alert:814971914086121472>' +
                                       '<a:yee:814971872503529473>')
        return


#A cmd to see whats new with the bot
@bot.command(name='news',
             help='Tells the bot to give you update on his changes')
async def news(ctx):
    if ctx.message.content.startswith('sir news'):
        await ctx.message.channel.send(
            'I am Sir Doge. Born on 2/3/2022, I can now roll dice, got a magic 8 ball, and got a new job at Jillamy. Type [sir help] for the current command list. Oh I can also yell at Nikhil.'
        )
        return


#beginning of the weather command

api_key = os.getenv('WEATHER_TOKEN')
base_url = "http://api.openweathermap.org/data/2.5/weather?"


#weather cmd
@bot.command(help='gives the weather for a given city at current time')
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel

    if x["cod"] != "404":
        async with channel.typing():

            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_fahrenheit = str(
                round(1.8 * (current_temperature - 273.15) + 32))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            weather_description = z[0]["description"]
            embed = discord.Embed(
                title=f"Weather in {city_name}",
                color=ctx.guild.me.top_role.color,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(name="Descripition",
                            value=f"**{weather_description}**",
                            inline=False)
            embed.add_field(name="Temperature(F)",
                            value=f"**{current_temperature_fahrenheit}°F**",
                            inline=False)
            embed.add_field(name="Humidity(%)",
                            value=f"**{current_humidity}%**",
                            inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)",
                            value=f"**{current_pressure}hPa**",
                            inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")

        await channel.send(embed=embed)
    else:
        await channel.send("City not found.")


#imgflippy
#still a work in progress got to reread the documentation
username = 'ThePalad1n'
password = 'AlphaBeta321!'

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

#Fetch the available memes
data = requests.get(
    'https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{
    'name': image['name'],
    'url': image['url'],
    'id': image['id']
} for image in data]


#List all the memes
@bot.command(name='memetypes',
             help='TBA: Tells the bot to list all the meme templetes')
async def memetypes(ctx):
    if ctx.message.content.startswith('sir memetypes'):
        await ctx.message.channel.send(
            'Here is the list of available memes : \n')
        ctr = 1

        for img in images:
            a = ctr, img['name']
            await ctx.message.channel.send(a)
            ctr = ctr + 1
        return


@bot.command(name='memehelp',
             help='TBA: Tells the bot to explain how to make a meme')
async def memehelp(ctx):
    if ctx.message.content.startswith('sir memetypes'):
        await ctx.message.channel.send(
            'I heard you needed help with making memes : \n')
        await ctx.message.channel.send(
            '1) first enter the serial number of the meme \n')
        await ctx.message.channel.send('2) Enter first text: \n')
        await ctx.message.channel.send('3) Enter second text: \n')
        await ctx.message.channel.send('Ex: [sir makememe 10 text1 text2')
        await ctx.message.channel.send(
            'Now just type [sir makememe] to get started')


@bot.command(name='makememe', help='TBA: Tells the bot to make a meme')
async def makememe(ctx, id: int, text0: str, text1: str):
    #Fetch the generated meme
    if ctx.message.content.startswith('sir makememe'):
        id = id
        text0 = text0
        text1 = text1
        URL = 'https://api.imgflip.com/caption_image'
        params = {
            'username': username,
            'password': password,
            'template_id': images[id - 1]['id'],
            'text0': text0,
            'text1': text1
        }
        response = requests.request('POST', URL, params=params).json()
        await ctx.message.channel.send(response)
        opener = urllib.request.URLopener()
        await ctx.message.channel.send(opener)
        await ctx.message.channel.send('Memeo CompleteO ')
        em = discord.Embed(title="Image")
        em.set_image(url=response["data"][0]["URL"])
        try:
            await ctx.message.chennel.send(embed=em)
        except:
            await ctx.message.channel.send("Derp")


keep_alive()
bot.run(os.getenv('TOKEN'))
