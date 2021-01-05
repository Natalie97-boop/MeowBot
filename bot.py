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
    if message.author == bot.user:
        return
    if message.content == "MeowCount":
        with open(f"{guild_name} .txt"), "r") as f:
            num = int(f.readline()) + 1
            return await message.channel.send(f"{num} Meows have been served")
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
