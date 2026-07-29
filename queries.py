import sqlite3

connection = sqlite3.connect("kingdom.db")
cursor = connection.cursor()

cursor.execute("PRAGMA integrity_check;")

print(cursor.fetchone())

connection.close()