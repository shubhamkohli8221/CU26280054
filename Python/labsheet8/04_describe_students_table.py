# 4. Display structure of students table.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        columns = con.execute("PRAGMA table_info(students)").fetchall()
    if columns:
        for col in columns:
            print(f"Name: {col[1]}, Type: {col[2]}, Primary key: {bool(col[5])}")
    else:
        print("Table not found. Run program 3 first.")
except sqlite3.Error as e:
    print("Database error:", e)
