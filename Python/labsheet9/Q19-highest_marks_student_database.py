import sqlite3
# Find the student with the maximum marks.
try:
    with sqlite3.connect("crud_students.db") as con:
        row = con.execute(
            "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
        ).fetchone()
    print("Highest scorer:", row if row else "No student records.")
except sqlite3.Error as error:
    print("Database error:", error)
