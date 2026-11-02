# Q28. Create a nested dictionary for student details.
students = {
    "student1": {"Name": "Aman", "Roll": 1, "Marks": 82},
    "student2": {"Name": "Riya", "Roll": 2, "Marks": 91}
}

for student_id, details in students.items():
    print(student_id, ":", details)
