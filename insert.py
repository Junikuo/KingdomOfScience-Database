import sqlite3

connection = sqlite3.connect("kingdom.db")
cursor = connection.cursor()

command_insert = """
INSERT INTO Character_Inventions (id, character_id, invention_id, contribution)

VALUES
(1, 1, 1, 'Creator'),
(2, 1, 2, 'Creator'),
(3, 1, 3, 'Creator'),
(4, 8, 3, 'Builder'),
(5, 1, 4, 'Creator'),
(6, 5, 4, 'Assistant'),
(7, 1, 5, 'Creator'),
(8, 8, 5, 'Builder'),
(9, 1, 6, 'Creator'),
(10, 8, 6, 'Builder'),
(11, 1, 7, 'Creator'),
(12, 5, 7, 'Co-creator'),
(13, 8, 7, 'Builder'),
(14, 1, 8, 'Creator'),
(15, 8, 8, 'Builder'),
(16, 11, 9, 'Captain'),
(17, 1, 9, 'Designer'),
(18, 11, 10, 'Captain'),
(19, 8, 10, 'Builder'),
(20, 1, 10, 'Designer'),
(21, 8, 11, 'Blacksmith'),
(22, 1, 12, 'Creator'),
(23, 12, 12, 'Chef'),
(24, 1, 13, 'Creator'),
(25, 5, 13, 'Assistant'),
(26, 1, 14, 'Creator'),
(27, 10, 14, 'Operator'),
(28, 1, 15, 'Creator');
"""

cursor.execute(command_insert)

connection.commit()
connection.close()