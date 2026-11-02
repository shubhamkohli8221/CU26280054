# 8. Insert one student record.
import sqlite3
try:
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with sqlite3.connect("student_db.db") as con:
        con.execute("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    print("Student inserted.")
except (ValueError, sqlite3.Error) as e:
    print("Input/database error:", e)
