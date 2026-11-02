# 12. Show students scoring more than 80.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT * FROM students WHERE marks > ?", (80,)).fetchall()
    for row in rows: print(row)
    if not rows: print("No students scored above 80.")
except sqlite3.Error as e:
    print("Database error:", e)
