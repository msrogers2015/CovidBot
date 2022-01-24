#!/usr/bin/env python3
import os
import discord
import requests
import aiosqlite
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='...')
bot.remove_command('help')


@bot.event
async def on_ready():
	print('Bot is online')

@commands.command()
async def get_record(self, ctx):
	db = await aiosqlite.connect('/home/mrogers/Documents/Fiverr_Template/cogs/covid.db')
	cursor = await db.execute("SELECT * FROM countries WHERE Country='United States of America'")
	row = await cursor.fetchone()
	print(row)
	await db.close()
#@tasks.loop(seconds=2.0)
#async def foo():
#	print('This is a repeat task')
#foo.start()

bot.run(TOKEN)