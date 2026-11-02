# 7. Check whether a table exists.
import sqlite3
table = input("Enter table name: ").strip()
try:
    with sqlite3.connect("student_db.db") as con:
        row = con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone()
    print("Table exists." if row else "Table does not exist.")
except sqlite3.Error as e:
    print("Database error:", e)
