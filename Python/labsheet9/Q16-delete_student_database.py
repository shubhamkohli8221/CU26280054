import sqlite3
# Delete one student record using its roll number.
try:
    roll = int(input("Roll number to delete: "))
    with sqlite3.connect("crud_students.db") as con:
        cur = con.execute("DELETE FROM students WHERE id=?", (roll,))
    print("Student deleted." if cur.rowcount else "Student not found.")
except ValueError:
    print("Roll number must be an integer.")
except sqlite3.Error as error:
    print("Database error:", error)
