# 24. Find average marks.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        avg = con.execute("SELECT AVG(marks) FROM students").fetchone()[0]
    print("Average marks:", avg if avg is not None else "No records found.")
except sqlite3.Error as e:
    print("Database error:", e)
