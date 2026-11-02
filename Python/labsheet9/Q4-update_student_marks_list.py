# Update marks for the matching roll number in a list.
students = [
    {"roll": 1, "name": "Asha", "age": 20, "marks": 88.5},
    {"roll": 2, "name": "Ravi", "age": 21, "marks": 76.0},
]
try:
    roll = int(input("Roll number: "))
    new_marks = float(input("New marks: "))
    student = next((s for s in students if s["roll"] == roll), None)
    if student:
        student["marks"] = new_marks
        print("Updated:", student)
    else:
        print("Roll number not found.")
except ValueError:
    print("Enter a valid roll number and marks.")
