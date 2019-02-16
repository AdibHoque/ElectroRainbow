import discord
from discord.ext import commands
import asyncio
import colorsys
import random
import time
import os
import json
import aiohttp
import datetime
from discord import Game, Embed, Color, Status, ChannelType
import dbl
import logging

bot = commands.Bot(command_prefix=commands.when_mentioned_or('er!'))
bot.remove_command("help")

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='Made with love by @ADIB HOQUE#6969', url='https://twitch.tv/myname', type=1))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='Upvote my bro ELECTRO', url='https://twitch.tv/myname', type=1))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='Add ELECTRO in your server', url='https://twitch.tv/myname', type=1))
        await asyncio.sleep(5)
        
async def rgb_task():
    while True:
    	role = discord.utils.get(server.roles, name="Rainbow")
    	await bot.edit_role(role, colour=discord.Colour(0x1abc9c))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x11806a))
    	await asyncio.sleep(2)
    	await bot.edit_role(rgb_list,colour=discord.Colour(0x2ecc71))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x1f8b4c))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x3498db))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x206694))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x9b59b6))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x71368a))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xe91e63))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xad1457))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xf1c40f))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xc27c0e))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xe67e22))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xa84300))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0xe74c3c))
    	await asyncio.sleep(2)
    	await bot.edit_role(role, colour=discord.Colour(0x992d22))
    	await asyncio.sleep(2)
	      
@bot.event
async def on_ready():
    print('the bot is ready')
    print(bot.user.name)
    print(bot.user.id)
    print('working properly')
    bot.loop.create_task(status_task())
    bot.loop.create_task(rgb_task())

def is_owner(ctx):
    return ctx.message.author.id == "488353416599306270"
    
def is_masstyper(ctx):
    return ctx.message.author.id == "488353416599306270, 517729298355060736"      
 																
@bot.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    await bot.say("Pong! {}ms".format(round((t2-t1)*1000)))

@bot.command(pass_context = True)
async def help(ctx):
	await bot.say('u pool there is no command except ping')
	
@bot.command(pass_context=True)
@commands.check(is_owner)
async def masstype(ctx, *, message=None):
    message = message or "Please specify a word to masstype!"
    await bot.delete_message(ctx.message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)
    await bot.say(message)

bot.run(os.getenv('Token'))
