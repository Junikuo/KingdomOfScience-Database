import sqlite3

connection = sqlite3.connect('kingdom.db')

cursor = connection.cursor()

command_create = """ 
CREATE TABLE Inventions (
    id INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT);"""

cursor.execute(command_create)

connection.commit()
connection.close()

