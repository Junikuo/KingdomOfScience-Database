import sqlite3

connection = sqlite3.connect('kingdom.db')

cursor = connection.cursor()

command1 = """ 
CREATE TABLE Inventions(
id INTEGER PRIMAY KEY,
Name TEXT,
Description TEXT);"""

cursor.execute(command1)

connection.commit
connection.close

