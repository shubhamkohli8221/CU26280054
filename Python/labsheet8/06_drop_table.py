# 6. Drop a table (requires confirmation).
import sqlite3
table = input("Table to drop (students/courses): ").strip().lower()
if table not in ("students", "courses"):
    print("Invalid table name.")
elif input(f"Type YES to drop {table}: ") == "YES":
    try:
        with sqlite3.connect("student_db.db") as con:
            con.execute(f"DROP TABLE IF EXISTS {table}")
        print("Table dropped.")
    except sqlite3.Error as e:
        print("Database error:", e)
else:
    print("Cancelled.")
