# Delete a student by roll number from the list.
students = [
    {"roll": 1, "name": "Asha", "age": 20, "marks": 88.5},
    {"roll": 2, "name": "Ravi", "age": 21, "marks": 76.0},
]
try:
    roll = int(input("Roll number to delete: "))
    before = len(students)
    students[:] = [s for s in students if s["roll"] != roll]
    print("Student deleted." if len(students) < before else "Roll number not found.")
    print("Remaining:", students)
except ValueError:
    print("Roll number must be an integer.")
