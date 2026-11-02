# 21. Create courses table and add sample courses.
import sqlite3
courses = [("Python Programming", "MCA"), ("Database Management", "MCA"), ("Web Development", "MCA")]
try:
    with sqlite3.connect("student_db.db") as con:
        con.execute("""CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL, department TEXT)""")
        con.executemany("INSERT INTO courses(course_name, department) VALUES (?, ?)", courses)
    print("Courses table created and sample courses inserted.")
except sqlite3.Error as e:
    print("Database error:", e)
