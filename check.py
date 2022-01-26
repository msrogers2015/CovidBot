#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('./covid.db')
cur = conn.cursor()
cur.execute('SELECt * FROM countries')
rows = cur.fetchall()

for row in rows:
	print(row)
