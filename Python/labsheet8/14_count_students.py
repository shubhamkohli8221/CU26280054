# 14. Count student records.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        count = con.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total students:", count)
except sqlite3.Error as e:
    print("Database error:", e)
