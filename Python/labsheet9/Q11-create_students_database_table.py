import sqlite3
# Create database and students table using SQLite.
try:
    with sqlite3.connect("crud_students.db") as con:
        con.execute("""CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY, name TEXT NOT NULL,
            age INTEGER NOT NULL, marks REAL NOT NULL)""")
    print("Database and students table are ready.")
except sqlite3.Error as error:
    print("Database error:", error)
