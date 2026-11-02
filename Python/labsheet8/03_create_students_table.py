# 3. Create students table.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        con.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, age INTEGER, marks REAL)""")
    print("Students table created.")
except sqlite3.Error as e:
    print("Database error:", e)
