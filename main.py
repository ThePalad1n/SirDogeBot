import discord
from discord.ext import commands
from discord.utils import get
import os
import requests
import json
import math
import urllib
import random
import time
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
    await client.change_presence(activity=discord.Streaming(
        name='Runescape', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@bot.command()
async def pushP(ctx):
    print('We have logged in as {0.user}'.format(client))
    await bot.change_presence(activity=discord.Game(name="Halo Infinite"))
    time.sleep(5)
    await ctx.send('Task Complete!')


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
async def barps(ctx, members: commands.Greedy[discord.Member]):
    slapped = ", ".join(x.name for x in members)
    await ctx.message.channel.send('NO NIKHIL!')
    await ctx.send('Nikhil just got slapped by Barps!')


#silly starwars meme cmd
@bot.command(name='hmp', help='unlimited power meme')
async def hmp(ctx):
    if ctx.message.content.startswith('sir hmp'):
        await ctx.message.channel.send('UNLIMITED POWER!')
        return


#patCount = 0
#sill cmd for bot reward
@bot.command(name='goodboi', help='Reward the bot for a good job')
async def goodboi(ctx):
    #patCount =+ 1
    if ctx.message.content.startswith('sir goodboi'):
        await ctx.message.channel.send('*Pat Pat*')
        #await ctx.message.channel.send('Sir Doge has been praised %d times!' % (patCount))
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


#silly meme cmd
@bot.command(name='backflip', help='another meme cmd')
async def backflip(ctx):
    if ctx.message.content.startswith('sir backflip'):
        await ctx.message.channel.send('Dogs dont do backflips')
        return


#silly meme cmd
@bot.command(name='mom', help='another meme cmd')
async def mom(ctx):
    if ctx.message.content.startswith('sir mom'):
        await ctx.message.channel.send('Your mom')
        return


#silly work command
@bot.command(name='jillamy', help='The cult')
async def jillamy(ctx):
    if ctx.message.content.startswith('sir jillamy'):
        await ctx.message.channel.send('<a:alert:814971914086121472>' +
                                       'Go Jillamy Go!!!' +
                                       '<a:alert:814971914086121472>')
        time.sleep(1)
        await ctx.message.channel.send('one of us')
        time.sleep(1)
        await ctx.message.channel.send('One Of Us')
        time.sleep(1)
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


#silly slap cmd
@bot.command(name="slap", help="sir slap @person, reason for slapping ")
async def slap(ctx,
               members: commands.Greedy[discord.Member],
               *,
               reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    if (slapped == 'nikheat1#0391'):
        await ctx.send('No Nikhil')
        await ctx.send('{} just got slapped by Barps'.format(slapped))
    else:
        await ctx.send('{} just got slapped for {}'.format(slapped, reason))


#poll cmd
reactions = ["👍", "👎"]
@bot.command(name="poll", help="a cmd to create a poll.")
async def poll(ctx, *, question):
    m = await ctx.send(f"Poll: {question} -{ctx.author}")
    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await m.add_reaction(emoji or name)


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


#========================================================================
#Dnd section
@bot.command(name='d100', help='dnd roll a d100')
async def d100(ctx):
    if ctx.message.content.startswith('sir d100'):
        await ctx.message.channel.send("Rolling D100")
        value = random.randint(1, 100)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d20', help='dnd roll a d20')
async def d20(ctx):
    if ctx.message.content.startswith('sir d20'):
        await ctx.message.channel.send("Rolling D20")
        value = random.randint(1, 20)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d12', help='dnd roll a d12')
async def d12(ctx):
    if ctx.message.content.startswith('sir d12'):
        await ctx.message.channel.send("Rolling D12")
        value = random.randint(1, 12)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d10', help='dnd roll a d10')
async def d10(ctx):
    if ctx.message.content.startswith('sir d10'):
        await ctx.message.channel.send("Rolling D10")
        value = random.randint(1, 10)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d8', help='dnd roll a d8')
async def d8(ctx):
    if ctx.message.content.startswith('sir d8'):
        await ctx.message.channel.send("Rolling D8")
        value = random.randint(1, 8)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d6', help='dnd roll a d6')
async def d6(ctx):
    if ctx.message.content.startswith('sir d6'):
        await ctx.message.channel.send("Rolling D6")
        value = random.randint(1, 6)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d4', help='dnd roll a d4')
async def d4(ctx):
    if ctx.message.content.startswith('sir d4'):
        await ctx.message.channel.send("Rolling D4")
        value = random.randint(1, 4)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


@bot.command(name='d2', help='dnd roll a d2')
async def d2(ctx):
    if ctx.message.content.startswith('sir d2'):
        await ctx.message.channel.send("Rolling D2")
        value = random.randint(1, 2)
        await ctx.message.channel.send("You rolled a % d " % (value))
        await ctx.message.channel.send("Add modifiers")


dndBaseURL = "https://www.dnd5eapi.co/api/"


@bot.command(help='grants dnd info')
async def query(ctx, s1: str, s2: str, s3: str):
    completeDND_url = dndBaseURL + s1 + '/' + s2
    response = requests.get(completeDND_url)
    x = response.json()
    y = x.get(s3)
    await ctx.message.channel.send(y)

@bot.command(name='plshelp', help='grants dnd api info')
async def plshelp(ctx):
    await ctx.message.channel.send(
        "You can search the following things:\n"
        "ability-scores, skills, proficiencies, languages, alignment, background, classes, features, races, equipment-categories, spells, feats, monsters.\n"
        "Follow these with the subcriteria ex: 'ability-scores/dex'\n"
        "Subclass help will be added soon. For now just follow last entry with /yoursubsearch \n"
    )


#want to add a query for dnd info related to classes and what not.
#probably better to add a DB for that amount of info
#could also modify the roles to be dependant of specific users modifiers
#additionally could simplify with having the max range as a var and take the cmd number

#=========================================================================

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
    if ctx.message.content.startswith('sir memehelp'):
        await ctx.message.channel.send(
            'I heard you needed help with making memes : \n')
        await ctx.message.channel.send(
            '1) first enter the serial number of the meme \n')
        await ctx.message.channel.send('2) Enter first text: \n')
        await ctx.message.channel.send('3) Enter second text: \n')
        await ctx.message.channel.send('Ex: [sir makememe 10 text1 text2]')
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
        r = response.get('data')
        z = r.get('url')
        await ctx.message.channel.send(z)
        await ctx.message.channel.send('Memeo CompleteO ')


keep_alive()
bot.run(os.getenv('TOKEN'))
