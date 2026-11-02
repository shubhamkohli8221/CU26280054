# Search a list of student dictionaries by name (case-insensitive).
students = [
    {"roll": 1, "name": "Asha", "age": 20, "marks": 88.5},
    {"roll": 2, "name": "Ravi", "age": 21, "marks": 76.0},
]
target = input("Student name to search: ").strip().casefold()
matches = [s for s in students if s["name"].casefold() == target]
print(*matches, sep="\\n") if matches else print("Student not found.")
