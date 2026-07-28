import sqlite3

connection = sqlite3.connect("kingdom.db")
cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM Inventions;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)