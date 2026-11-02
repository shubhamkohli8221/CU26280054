# Program 29: Search for a student by name in a CSV file.
import csv

target = input("Enter student name to search: ").strip().casefold()
try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        matches = [
            row for row in csv.DictReader(file)
            if row.get("Name", "").strip().casefold() == target
        ]
    if matches:
        for student in matches:
            print(student)
    else:
        print("Student not found.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_csv.py first.")
