# 18. Delete a student by ID.
import sqlite3
try:
    sid = int(input("Student ID to delete: "))
    if input("Type YES to confirm: ") == "YES":
        with sqlite3.connect("student_db.db") as con:
            cur = con.execute("DELETE FROM students WHERE id=?", (sid,))
        print("Deleted." if cur.rowcount else "Student ID not found.")
    else: print("Cancelled.")
except (ValueError, sqlite3.Error) as e:
    print("Input/database error:", e)
