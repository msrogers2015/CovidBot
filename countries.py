#!/usr/bin/env python3
import sqlite3
import aiosqlite
import requests
'''
r = requests.get('https://api.covid19api.com/summary')
data = r.json()
conn = sqlite3.connect('covid.db')
cur = conn.cursor()
countries = data['Countries']
for country in countries:
    Country = str(country['Country'])
    NewConfirmed = int(country['NewConfirmed'])
    TotalConfirmed = int(country['TotalConfirmed'])
    NewDeaths = int(country['NewDeaths'])
    TotalDeaths = int(country['TotalDeaths'])
    NewRecovered = int(country['NewRecovered'])
    TotalRecovered = int(country['TotalRecovered'])
    cur.execute("""INSERT INTO countries(Country,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered) VALUES(?,?,?,?,?,?,?)""",(Country,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered))
conn.commit()
conn.close()
print('Finished')
'''
async def get_record():
    db = await aiosqlite.connect('covid.db')
    cursor = await db.execute("SELECT * WHERE Country='United States of America'")
    row = await cursor.fetchone()
    print(row)
    await db.close()

get_record()