# 5. List all tables in the database.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
    print("Tables:", [r[0] for r in rows])
except sqlite3.Error as e:
    print("Database error:", e)
