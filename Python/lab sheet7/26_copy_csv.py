# Program 26: Copy all rows from one CSV file into another CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as source:
        rows = list(csv.reader(source))
    with open("students_copy.csv", "w", newline="", encoding="utf-8") as destination:
        csv.writer(destination).writerows(rows)
    print("Data copied to students_copy.csv.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_csv.py first.")
