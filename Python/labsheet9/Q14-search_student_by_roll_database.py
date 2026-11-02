import sqlite3
# Retrieve one student using the roll number / primary key.
try:
    roll = int(input("Roll number: "))
    with sqlite3.connect("crud_students.db") as con:
        row = con.execute("SELECT * FROM students WHERE id=?", (roll,)).fetchone()
    print(row if row else "Student not found.")
except ValueError:
    print("Roll number must be an integer.")
except sqlite3.Error as error:
    print("Database error:", error)
