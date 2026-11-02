# 10. Display all students.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()
    for row in rows:
        print(row)
    if not rows: print("No records found.")
except sqlite3.Error as e:
    print("Database error:", e)
