import sqlite3

def create_database():
	conn = sqlite3.connect('./covid.db')
	cur = conn.cursor()
	cur.execute('''CREATE TABLE countries(
			Country TEXT PRIMARY KEY,
			NewConfirmed INTEGER,
			TotalConfirmed INTEGER,
			NewDeaths INTEGER,
			TotalDeaths INTEGER,
			NewRecovered INTEGER,
			TotalRecovered INTEGER);''')
	conn.commit()
	conn.close()
	print('Database Created')

create_database()
