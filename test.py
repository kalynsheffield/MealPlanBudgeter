import sqlite3

conn = sqlite3.connect('meals.db')

c = conn.cursor()

# """""" = DOT STRING
#c.execute("""CREATE TABLE meals(
#         place TEXT,
#          meal TEXT,
#          price REAL
#          )""")

#c.execute("INSERT INTO mealS VALUES('Euerka', 'Spicy Chicken Sandwich', 11.00)")

#conn.commit()

c.execute("SELECT * FROM meals WHERE place='Euerka'")

#fetches one row from results
#fetchmany(#) returns # rows from results as list
#fetchall returns all as list
print(c.fetchall())
conn.commit()
conn.close()