import sqlite3

connection = sqlite3.connect('kingdom.db')
cursor = connection.cursor()

command_insert = """
INSERT INTO Inventions
Values
(1, 'Soap', 'Basic hygiene product made from natural ingredients'),
(2, 'Gunpowder', 'Explosive mixture used for weapons and mining'),
(3, 'Glass', 'Transparent material used for containers and lenses'),
(4, 'Medicine', 'Sulfa drug used to cure pneumonia'),
(5, 'Electric Generator', 'Device that produces electricity'),
(6, 'Light Bulb', 'Electric lamp for illumination'),
(7, 'Telephone', 'Communication device using electrical signals'),
(8, 'Steam Engine', 'Machine powered by steam pressure'),
(9, 'Hot Air Balloon', 'Aircraft lifted by heated air'),
(10, 'Perseus', 'Advanced sailing ship built for exploration'),
(11, 'Katana', 'Traditional Japanese sword'),
(12, 'Ramen', 'Nutritious noodle dish'),
(13, 'Camera', 'Device used to capture photographs'),
(14, 'Radio', 'Wireless communication system'),
(15, 'Drone', 'Small remote-controlled flying device');
"""
cursor.execute(command_insert)
connection.commit
connection.close