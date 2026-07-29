import sqlite3

connection = sqlite3.connect("kingdom.db")
cursor = connection.cursor()

command_insert = """
INSERT INTO Materials (id, name, category, rarity)

VALUES
(1, 'Stone', 'Mineral', 'Common'),
(2, 'Wood', 'Plant', 'Common'),
(3, 'Clay', 'Mineral', 'Common'),
(4, 'Sand', 'Mineral', 'Common'),
(5, 'Glass', 'Mineral', 'Uncommon'),
(6, 'Iron', 'Metal', 'Uncommon'),
(7, 'Copper', 'Metal', 'Uncommon'),
(8, 'Coal', 'Fuel', 'Common'),
(9, 'Sulfur', 'Chemical', 'Rare'),
(10, 'Limestone', 'Mineral', 'Common'),
(11, 'Cotton', 'Plant', 'Common'),
(12, 'Bamboo', 'Plant', 'Common'),
(13, 'Gold', 'Precious Metal', 'Rare'),
(14, 'Silver', 'Precious Metal', 'Rare'),
(15, 'Tungsten', 'Metal', 'Rare'),
(16, 'Platinum', 'Precious Metal', 'Legendary'),
(17, 'Nitric Acid', 'Chemical', 'Rare'),
(18, 'Alcohol', 'Chemical', 'Uncommon'),
(19, 'Charcoal', 'Fuel', 'Common'),
(20, 'Manganese', 'Metal', 'Rare');
"""

cursor.execute(command_insert)

connection.commit()
connection.close()