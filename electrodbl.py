import discord
import asyncio
import aiohttp
import dbl
import logging
import datetime
import json
import os
import time
from discord.ext import commands

bot = commands.Bot 

dbltoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxMDQ5MTI0MzE1NTgxNjQ0OSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTQ2NDExNzYxfQ.V_7sJcSceSDB93OR5ZaTkoGHQqQN2ic2uO7U8cSeQlM"
url = "https://discordbots.org/api/bots/510491243155816449/stats"
headers = {"Authorization" : dbltoken}

@bot.event()
async def on_ready():
    payload = {"server_count"  : len(bot.servers)}
    async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)

@bot.event()            
async def on_server_join(server):
    payload = {"server_count"  : len(bot.servers)}
    async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)

@bot.event()     
async def on_server_remove(server):
    payload = {"server_count"  : len(bot.servers)}
    async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)

bot.run(os.getenv('Token'))
