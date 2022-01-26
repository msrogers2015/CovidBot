#!/usr/bin/env python3
import os
import discord
import requests
import sqlite3
import aiosqlite
from discord.ext import commands, tasks
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='coviddat')
bot.remove_command('help')


@bot.event
async def on_ready():
	print('Bot is online')
	
@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f'{round(bot.latency*1000)}ms', color=embed_color)
    await ctx.send(embed=embed)



@bot.command()
async def aping(ctx):
	embed = discord.Embed(title="Pong!", description=f'{round(bot.latency*1000)}ms', color=0xfff)
	await ctx.send(embed=embed)


@bot.command()
async def a(ctx, *, location):
	db = await aiosqlite.connect('./covid.db')
	cursor = await db.execute("SELECT * FROM countries WHERE Country=?",(location,))
	row = await cursor.fetchone()
	async with ctx.typing():
		embed = discord.Embed(title=f"Covid Data For {location.title()}")
		embed.set_image(url="https://c.pxhere.com/images/05/8c/4ffd8a6f1edd688a094a64e24ebd-1608796.jpg!d")
		embed.add_field(name='Country',value=row[0], inline=False)
		embed.add_field(name='New Comfirmed Cases', value=format(row[1],',d'), inline=False)
		embed.add_field(name='Total Confirmed Cases', value=format(row[2],',d'), inline=False)
		embed.add_field(name='New Deaths', value=format(row[3],',d'), inline=False)
		embed.add_field(name="Total Deaths",value=format(row[4],',d'), inline=False)
		embed.add_field(name='New Recovery Cases',value=format(row[5],',d'), inline=False)
		embed.add_field(name='Total Recovery Cases', value=format(row[6],',d'), inline=False)
		DeathRate = round(((row[4]/row[2])*100),2)
		RecoverRate = round(((row[6]/row[2])*100),2)
		embed.add_field(name='Total Death Rate', value=str(DeathRate)+'%', inline=False)
		embed.add_field(name='Total Recovery Rate', value=str(RecoverRate)+'%', inline=False)
		#time.sleep(5)
	await ctx.send(embed=embed)
	await db.close()



#@tasks.loop(minutes=1440)
async def info_update():
	r = requests.get('https://api.covid19api.com/summer')
	data = r.json()
	countries = data['Countries']
	print('Starting update')
	conn = sqlite3.connect('./covid.db')
	cur = conn.cursor()
	for country in countries:
		Country = str(country['Country'])
		NewConfirmed = int(country['NewConfirmed'])
		TotalConfirmed = int(country['TotalConfirmed'])
		NewDeaths = int(country['NewDeaths'])
		TotalDeaths = int(country['TotalDeaths'])
		NewRecovered = int(country['NewRecovered'])
		TotalRecovered = int(country['TotalRecovered'])
		print(f'Updating {Country}')
		cur.execute('''UPDATE countries SET NewConfirmed=?, TotalConfirmed=?,
				NewDeaths=?, TotalDeaths=?, NewRecovered=?, TotalRecovered=? 
				WHERE Country=?''',(NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Country)
	    	print(f'{Country} updated')
	print('Database updated')

	

bot.run(TOKEN)
