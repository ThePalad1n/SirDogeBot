import discord
from discord.ext import commands
import os
import requests
import json
import math
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

@bot.command(name='c', help='Tells the bot to c')
async def c(ctx):
  if ctx.message.content.startswith('sir c'):
        await ctx.message.channel.send('C o n g r a t s!')
        await ctx.message.channel.send('<a:ye:814971851485872140>' + '<a:catjam:824878456939610112>'+'<a:beat:814971891969294396>'+
        '<a:alert:814971914086121472>'+'<a:yee:814971872503529473>')
        return

@bot.command(name='news', help='Tells the bot to give you update on his changes')
async def news(ctx):
  if ctx.message.content.startswith('sir news'):
        await ctx.message.channel.send('Born on 4/1/2021, got a few cmds, but lookin to add memes soon. type [sir help] for the current command list.')
        return


api_key = os.getenv('WEATHER_TOKEN')
base_url = "http://api.openweathermap.org/data/2.5/weather?"


#weather cmd
@bot.command()
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
        current_temperature_fahrenheit = str(round(1.8*(current_temperature - 273.15)+32))
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        weather_description = z[0]["description"]
        embed = discord.Embed(title=f"Weather in {city_name}",
                          color=ctx.guild.me.top_role.color,
                          timestamp=ctx.message.created_at,)
        embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
        embed.add_field(name="Temperature(F)", value=f"**{current_temperature_fahrenheit}°F**", inline=False)
        embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
        embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
        embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
        embed.set_footer(text=f"Requested by {ctx.author.name}")

    await channel.send(embed=embed)
  else:
      await channel.send("City not found.")


keep_alive()
bot.run(os.getenv('TOKEN'))