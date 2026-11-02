# 22. Perform an INNER JOIN between students and courses.
# This example matches students.id with courses.course_id.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("""SELECT s.id, s.name, c.course_name
            FROM students s INNER JOIN courses c ON s.id = c.course_id""").fetchall()
    for row in rows: print(row)
    if not rows: print("No matching IDs. The join condition is an example.")
except sqlite3.Error as e:
    print("Database error:", e)
