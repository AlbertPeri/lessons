import sqlite3
conn = sqlite3.connect("games.db")
curs = conn.cursor()

# curs.execute("SELECT * FROM top_games")
# rows = curs.fetchall()
# print(rows)

rows = curs.execute("SELECT name, rating FROM top_games ORDER BY rating DESC")
for row in rows:
	print("Название команды: {0[0]}, рейтинг: {0[1]}".format(row))

# curs.execute("UPDATE top_games SET rating = 1.1 WHERE name = 'ГТА 5'")
# curs.execute("DELETE FROM top_games WHERE name = 'Аутлас'")
# conn.commit()

# curs.execute("SELECT * FROM top_games")
# rows = curs.fetchall()
# print(rows)

aye = int(input("Что вывести?: "))
if aye == 1:
	print("Реал Мадрид', 29, 'футбол'")
elif aye == 2:
	print("Барселона', 28, 'футюол'")

curs.close()
conn.close()