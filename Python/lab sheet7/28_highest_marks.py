# Program 28: Find the student with the highest marks in a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        students = []
        for row in csv.DictReader(file):
            try:
                students.append((row["Name"], float(row["Marks"])))
            except (KeyError, ValueError):
                continue

    if students:
        name, marks = max(students, key=lambda student: student[1])
        print(f"Highest marks: {marks:g} by {name}")
    else:
        print("No valid student marks found.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_csv.py first.")
