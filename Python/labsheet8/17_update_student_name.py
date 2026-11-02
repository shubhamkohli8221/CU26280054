# 17. Update student's name using ID.
import sqlite3
try:
    sid = int(input("Student ID: "))
    name = input("New name: ").strip()
    with sqlite3.connect("student_db.db") as con:
        cur = con.execute("UPDATE students SET name=? WHERE id=?", (name, sid))
    print("Name updated." if cur.rowcount else "Student ID not found.")
except (ValueError, sqlite3.Error) as e:
    print("Input/database error:", e)
