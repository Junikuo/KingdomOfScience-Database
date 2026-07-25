import sqlite3

connection = sqlite3.connect('kingdom.db')

cursor = connection.cursor()

command_create = """ 
CREATE TABLE Materials (
    id INTEGER PRIMARY KEY,
    Name TEXT,
    Category TEXT,
    Rarity TEXT);"""

cursor.execute(command_create)

connection.commit
connection.close

