# Program 23: Calculate the average of each numeric CSV column.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        totals = {}
        counts = {}
        for row in reader:
            for column, value in row.items():
                try:
                    number = float(value)
                except (ValueError, TypeError):
                    continue
                totals[column] = totals.get(column, 0) + number
                counts[column] = counts.get(column, 0) + 1

    if totals:
        for column in totals:
            print(f"Average {column}: {totals[column] / counts[column]:.2f}")
    else:
        print("No numeric columns found.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_csv.py first.")
