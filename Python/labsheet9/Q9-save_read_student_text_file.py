# Save student records as simple pipe-separated text and read them back.
records = [
    {"roll": 1, "name": "Asha", "age": 20, "marks": 88.5},
    {"roll": 2, "name": "Ravi", "age": 21, "marks": 76.0},
]
try:
    with open("student_records.txt", "w", encoding="utf-8") as file:
        for s in records:
            file.write(f"{s['roll']}|{s['name']}|{s['age']}|{s['marks']}\\n")
    print("Saved records. Reading them back:")
    with open("student_records.txt", encoding="utf-8") as file:
        for line in file:
            roll, name, age, marks = line.rstrip("\\n").split("|")
            print({"roll": int(roll), "name": name, "age": int(age), "marks": float(marks)})
except (OSError, ValueError) as error:
    print("File/data error:", error)
