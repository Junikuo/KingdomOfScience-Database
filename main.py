import sqlite3

connection = sqlite3.connect('kingdom.db')

cursor = connection.cursor()

menu = """
========================================
    KINGDOM OF SCIENCE DATABASE
========================================

1. View Characters
2. View Inventions
3. View Character Contributions
4. View Materials
5. Exit
"""

print(menu)

while True:
     option = int(input("Select a option " ))

     if option == 1:
        command1 = """
        SELECT *
        FROM Characters;"""

        cursor.execute(command1)
        characters = cursor.fetchall()

        for character in characters:
            print(character)

     elif option == 2:
        command2 = """
        SELECT *
        FROM Inventions;"""

        cursor.execute(command2)
        inventions = cursor.fetchall()

        for invention in inventions:
            print(invention)

     elif option == 3:
        command3 = """
       SELECT 
     Characters.name,
     Inventions.name,
     Character_Inventions.contribution

     FROM Character_Inventions

     JOIN Characters
     ON Character_Inventions.character_id = Characters.id

     JOIN Inventions
     ON Character_Inventions.invention_id = Inventions.id;"""

        cursor.execute(command3)
        Character_Inventions = cursor.fetchall()

        for Character_Invention in Character_Inventions:
            print(Character_Invention)

     elif option == 4:
        command4 = """
        SELECT * 
        FROM Materials;"""

        cursor.execute(command4)

        Materials = cursor.fetchall()

        for Material in Materials:
            print(Material)

     elif option == 5:
        break

     else:
        print("Insert a valid option")



    
