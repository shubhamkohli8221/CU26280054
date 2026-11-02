# 25. Group students by age and count each group.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT age, COUNT(*) FROM students GROUP BY age ORDER BY age").fetchall()
    for age, count in rows: print(f"Age {age}: {count} student(s)")
except sqlite3.Error as e:
    print("Database error:", e)
