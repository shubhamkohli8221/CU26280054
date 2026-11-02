import sqlite3
# Update marks of the student identified by roll number.
try:
    roll = int(input("Roll number: "))
    marks = float(input("New marks: "))
    with sqlite3.connect("crud_students.db") as con:
        cur = con.execute("UPDATE students SET marks=? WHERE id=?", (marks, roll))
    print("Marks updated." if cur.rowcount else "Student not found.")
except ValueError:
    print("Enter numeric roll number and marks.")
except sqlite3.Error as error:
    print("Database error:", error)
