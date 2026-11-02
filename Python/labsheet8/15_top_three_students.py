# 15. Display top three students by marks.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3").fetchall()
    for row in rows: print(row)
except sqlite3.Error as e:
    print("Database error:", e)
