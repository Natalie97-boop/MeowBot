import os
import random
import re
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

TOKEN = 'REDACTED'
pattern = '[Mm][Ee][Oo][Ww]'
nyaa_pattern = '[Nn][Yy][Aa][Aa]'

description = '''MeowBot'''

bot = discord.Client()

@bot.event
async def on_ready():
    print("Meow")


@bot.event
async def on_message(message):
    guild_name = message.guild.name

    if message.author == bot.user:
        return
    
    if re.search(nyaa_pattern, message.content):
        file = random.choice(os.listdir("./Catgirl_pics"))
        await message.channel.send("OwO")
        await message.channel.send(file=discord.File("./Catgirl_pics/" + file))
        

    if message.content == "MeowCount":
        try:
            with open((guild_name + ".txt"),"r") as filehandle:
                num = filehandle.readline()
                num2 = int(num) + 1
                num3 = str(num2)
                await message.channel.send(num3 + " Meows have been served")
                return
        except:
            await message.channel.send("There have been no Meows in this server")

    if re.search(pattern, message.content):
        try:
            with open((guild_name + ".txt"),"r") as filehandle:
            	num = filehandle.readline()
            num2 = int(num) + 1
            num3 = str(num2)
            await message.channel.send("Meow :black_cat:")
            with open((guild_name + ".txt"),"w") as filehandle:
                filehandle.write(num3)
        except:
            with open((guild_name + ".txt"),"w") as filehandle:
                filehandle.write("1")
            await message.channel.send("Meow :black_cat:")
            await message.channel.send("First Meow! Woo!")
            
bot.run(TOKEN)
