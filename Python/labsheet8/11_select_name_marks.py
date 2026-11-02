# 11. Display only name and marks.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT name, marks FROM students").fetchall()
    for row in rows: print(row)
except sqlite3.Error as e:
    print("Database error:", e)
