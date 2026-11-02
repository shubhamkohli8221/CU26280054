# Display all records from a sample in-memory list.
students = [
    {"roll": 1, "name": "Asha", "age": 20, "marks": 88.5},
    {"roll": 2, "name": "Ravi", "age": 21, "marks": 76.0},
]
if students:
    for student in students:
        print(student)
else:
    print("No student records.")
