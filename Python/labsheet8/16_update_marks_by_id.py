# 16. Update marks using student ID.
import sqlite3
try:
    sid = int(input("Student ID: "))
    marks = float(input("New marks: "))
    with sqlite3.connect("student_db.db") as con:
        cur = con.execute("UPDATE students SET marks=? WHERE id=?", (marks, sid))
    print("Updated." if cur.rowcount else "Student ID not found.")
except (ValueError, sqlite3.Error) as e:
    print("Input/database error:", e)
