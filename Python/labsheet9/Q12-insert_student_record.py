import sqlite3
# Insert a student record into the students table.
try:
    values = (int(input("Roll/ID: ")), input("Name: ").strip(),
              int(input("Age: ")), float(input("Marks: ")))
    with sqlite3.connect("crud_students.db") as con:
        con.execute("INSERT INTO students VALUES (?, ?, ?, ?)", values)
    print("Student record created.")
except ValueError:
    print("Enter valid numeric ID, age and marks.")
except sqlite3.Error as error:
    print("Database error (run Q11 first):", error)
