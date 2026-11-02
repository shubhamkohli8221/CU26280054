# Program 21: Create a CSV file and write student records into it.
import csv

students = [
    ["Name", "Marks", "Age"],
    ["Aman", 85, 20],
    ["Riya", 92, 21],
    ["Karan", 76, 19],
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student data written to students.csv.")
