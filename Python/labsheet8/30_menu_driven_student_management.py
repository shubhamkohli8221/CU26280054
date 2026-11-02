# 30. Menu-driven student management: Add, View, Update, Delete, Exit.
import sqlite3

DB_NAME = "student_db.db"

def setup():
    with sqlite3.connect(DB_NAME) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, age INTEGER, marks REAL)""")

def add_student():
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with sqlite3.connect(DB_NAME) as con:
        con.execute("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    print("Student added.")

def view_students():
    with sqlite3.connect(DB_NAME) as con:
        rows = con.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()
    for row in rows: print(row)
    if not rows: print("No students found.")

def update_student():
    sid = int(input("Student ID to update: "))
    name = input("New name: ").strip()
    marks = float(input("New marks: "))
    with sqlite3.connect(DB_NAME) as con:
        cur = con.execute("UPDATE students SET name=?, marks=? WHERE id=?", (name, marks, sid))
    print("Student updated." if cur.rowcount else "Student ID not found.")

def delete_student():
    sid = int(input("Student ID to delete: "))
    if input("Type YES to confirm deletion: ") == "YES":
        with sqlite3.connect(DB_NAME) as con:
            cur = con.execute("DELETE FROM students WHERE id=?", (sid,))
        print("Student deleted." if cur.rowcount else "Student ID not found.")
    else:
        print("Cancelled.")

def main():
    setup()
    while True:
        print("\n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1": add_student()
            elif choice == "2": view_students()
            elif choice == "3": update_student()
            elif choice == "4": delete_student()
            elif choice == "5":
                print("Goodbye!")
                break
            else: print("Invalid choice.")
        except (ValueError, sqlite3.Error) as e:
            print("Input/database error:", e)

if __name__ == "__main__":
    main()
