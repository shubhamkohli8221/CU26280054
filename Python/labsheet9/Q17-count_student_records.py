import sqlite3
# Count the total number of student records.
try:
    with sqlite3.connect("crud_students.db") as con:
        total = con.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total records:", total)
except sqlite3.Error as error:
    print("Database error:", error)
