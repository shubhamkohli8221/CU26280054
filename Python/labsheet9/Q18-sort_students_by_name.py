import sqlite3
# Display records in ascending order by student name.
try:
    with sqlite3.connect("crud_students.db") as con:
        rows = con.execute("SELECT * FROM students ORDER BY name COLLATE NOCASE").fetchall()
    for row in rows: print(row)
except sqlite3.Error as error:
    print("Database error:", error)
