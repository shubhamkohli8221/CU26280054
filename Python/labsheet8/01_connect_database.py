# 1. Connect to SQLite database and show success.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        print("Database connected successfully.")
except sqlite3.Error as e:
    print("Database error:", e)
