# 27. Import student data from students_import.csv into students table.
# CSV format: name,age,marks (do not include a header row).
import sqlite3
import csv
try:
    with open("students_import.csv", newline="", encoding="utf-8") as file:
        records = []
        for row in csv.reader(file):
            if row and len(row) == 3:
                records.append((row[0], int(row[1]), float(row[2])))
    with sqlite3.connect("student_db.db") as con:
        con.executemany("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", records)
    print(f"Imported {len(records)} records.")
except (OSError, ValueError, sqlite3.Error) as e:
    print("Import error:", e)
