# 2. Create/open the student_db database file.
import sqlite3
try:
    with sqlite3.connect("student_db.db"):
        print("Database student_db.db created/opened successfully.")
except sqlite3.Error as e:
    print("Database error:", e)
