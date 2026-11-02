# 9. Insert multiple sample student records.
import sqlite3
students = [("Aman", 20, 85), ("Riya", 21, 92), ("Karan", 19, 76)]
try:
    with sqlite3.connect("student_db.db") as con:
        con.executemany("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", students)
    print("Multiple records inserted.")
except sqlite3.Error as e:
    print("Database error:", e)
