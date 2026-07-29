import sqlite3

connection = sqlite3.connect("kingdom.db")
cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM Character_Inventions;
""")

rows = cursor.fetchall()

print("Número de filas:", len(rows))
print(rows)

connection.close()