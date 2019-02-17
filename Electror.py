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
        await bot.change_presence(game=discord.Game(name='Upvote by big bro ELECTRO', url='https://twitch.tv/myname', type=1))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='Chaging color of rainbow role......', url='https://twitch.tv/myname', type=1))
        await asyncio.sleep(5)
        
@bot.event
async def on_ready():
  server = bot.get_server("508648651942264847")
  return server

async def runtime_background_task():
  colours = [0xFF0000, 0x00FF00, 0x0000FF]
  i = 0

  server = await on_ready()
  role = discord.utils.get(server.roles, name="Rainbow")

  while not bot.is_closed:
    i = (i + 1) % 3
    await bot.edit_role(server=server, role=role, colour=discord.Colour(colours[i]))

    await asyncio.sleep(2)
    bot.loop.create_task(runtime_background_task())
    bot.loop.create_task(status_task())

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