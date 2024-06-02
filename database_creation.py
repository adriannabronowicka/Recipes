import sqlite3

con = sqlite3.connect('recipes_database.db')

con.row_factory = sqlite3.Row

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Recipes(
            id INTEGER PRIMARY KEY ASC,
            recipes_name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            instruction TEXT NOT NULL
    )""")

con.commit()
con.close()
