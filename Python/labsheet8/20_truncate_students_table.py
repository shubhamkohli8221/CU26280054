# 20. Empty students table but preserve its structure.
# SQLite does not support TRUNCATE; DELETE FROM has the equivalent effect on rows.
import sqlite3
try:
    if input("Delete ALL students? Type YES: ") == "YES":
        with sqlite3.connect("student_db.db") as con:
            con.execute("DELETE FROM students")
        print("Table emptied; structure preserved.")
    else: print("Cancelled.")
except sqlite3.Error as e:
    print("Database error:", e)
