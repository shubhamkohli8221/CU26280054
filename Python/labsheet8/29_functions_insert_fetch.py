# 29. Use functions to insert and fetch student records.
import sqlite3

DB_NAME = "student_db.db"

def insert_student(name, age, marks):
    with sqlite3.connect(DB_NAME) as con:
        con.execute("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", (name, age, marks))

def fetch_students():
    with sqlite3.connect(DB_NAME) as con:
        return con.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()

try:
    insert_student("Sample Student", 20, 81)
    print("Inserted one sample student.")
    for student in fetch_students():
        print(student)
except sqlite3.Error as e:
    print("Database error:", e)
