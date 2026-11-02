# Q11. Create a dictionary of student names and marks.
students = {}
count = int(input("How many students? "))

for _ in range(count):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks")
for name, marks in students.items():
    print(f"{name}: {marks}")
