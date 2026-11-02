# 26. Export students table to a CSV file.
import sqlite3
import csv
try:
    with sqlite3.connect("student_db.db") as con:
        rows = con.execute("SELECT id, name, age, marks FROM students").fetchall()
    with open("students_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "age", "marks"])
        writer.writerows(rows)
    print("Exported data to students_export.csv.")
except (sqlite3.Error, OSError) as e:
    print("Export error:", e)
