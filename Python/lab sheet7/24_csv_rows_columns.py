# Program 24: Count data rows and columns in a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    if rows:
        print("Number of columns:", len(rows[0]))
        print("Number of data rows:", max(0, len(rows) - 1))  # Exclude header
    else:
        print("The CSV file is empty.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_csv.py first.")
