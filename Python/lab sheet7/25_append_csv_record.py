# Program 25: Append a new student record to an existing CSV file.
import csv
import os

filename = "students.csv"
try:
    file_exists_and_has_data = os.path.exists(filename) and os.path.getsize(filename) > 0
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists_and_has_data:
            writer.writerow(["Name", "Marks", "Age"])
        writer.writerow(["Neha", 88, 20])
    print("New record appended to", filename)
except OSError as error:
    print("File error:", error)
