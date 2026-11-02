import sqlite3
# Fetch and print every student record.
try:
    with sqlite3.connect("crud_students.db") as con:
        rows = con.execute("SELECT * FROM students ORDER BY id").fetchall()
    for row in rows: print(row)
    if not rows: print("No student records.")
except sqlite3.Error as error:
    print("Database error:", error)
