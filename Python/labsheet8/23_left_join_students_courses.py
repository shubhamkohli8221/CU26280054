# 23. Perform a LEFT JOIN between students and courses.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("""SELECT s.id, s.name, c.course_name
            FROM students s LEFT JOIN courses c ON s.id = c.course_id
            ORDER BY s.id""").fetchall()
    for row in rows: print(row)
except sqlite3.Error as e:
    print("Database error:", e)
