#!/usr/bin/env python3
import sqlite3
import requests


def info_update():
	r = requests.get('https://api.covid19api.com/summary')
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
		cur.execute('''UPDATE countries SET NewConfirmed=?, TotalConfirmed=?,
				NewDeaths=?, TotalDeaths=?, NewRecovered=?, TotalRecovered=? 
				WHERE Country=?''',(NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Country))
	print('Database updated')



info_update()
