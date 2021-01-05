import re
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

TOKEN = 'REDACTED'
pattern = '[Mm][Ee][Oo][Ww]'

description = '''MeowBot'''

bot = discord.Client()

@bot.event
async def on_ready():
    print("Meow")


@bot.event
async def on_message(message):
    guild_name = message.guild.name
    channel_name = message.channel.name
    if message.author == bot.user:
        return
    if message.content == "MeowCount":
        f = open((guild_name + " " + channel_name + ".txt"),"r")
        num = f.readline()
        num2 = int(num,10) + 1
        num3 = str(num2)
        await message.channel.send(num3 + " Meows have been served")
        f.close()
        return
    if re.search(pattern, message.content):
        try:
            with open((guild_name + " " + channel_name + ".txt"),"r") as filehandle:
            	num = filehandle.readline()
            num2 = int(num,10) + 1
            num3 = str(num2)
            await message.channel.send("Meow :black_cat:")
            with open((guild_name + " " + channel_name + ".txt"),"w") as filehandle:
                filehandle.write(num3)
        except:
            with open((guild_name + " " + channel_name + ".txt"),"w") as filehandle:
                filehandle.write("1")
            await message.channel.send("Meow :black_cat:")
            await message.channel.send("First Meow! Woo!")
bot.run(TOKEN)