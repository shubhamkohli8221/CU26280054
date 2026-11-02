# 28. Demonstrate database error handling.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as con:
        # Intentionally invalid table name to demonstrate an error.
        con.execute("SELECT * FROM table_that_does_not_exist")
except sqlite3.Error as e:
    print("Database error caught:", e)
