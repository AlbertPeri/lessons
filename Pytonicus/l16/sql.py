import sqlite3
conn = sqlite3.connect("games.db")
curs = conn.cursor()

curs.execute("""CREATE TABLE top_games (
name VARCHAR(60) PRIMARY KEY,
rating REAL,
genre VARCHAR(40)
)""")



curs.execute("INSERT INTO top_games VALUES('Реал Мадрид', 29, 'футбол')")
curs.execute("INSERT INTO top_games VALUES('Барселона', 28, 'футюол')")

name, rating, genre = 'Атлетико Мадрид', 23, 'футбол'
curs.execute("INSERT INTO top_games VALUES(?, ?, ?)", (name, rating, genre))

ins = "INSERT INTO top_games VALUES(?, ?, ?)"
data = 'Севилья', 21, 'футбол'
curs.execute(ins, data)
data = 'Вильярреал', 19, 'футбол'
curs.execute(ins, data)

conn.commit()

curs.close()
conn.close()