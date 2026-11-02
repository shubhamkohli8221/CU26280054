import sqlite3
DB = "crud_students.db"

def setup():
    with sqlite3.connect(DB) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY, name TEXT NOT NULL,
            age INTEGER NOT NULL, marks REAL NOT NULL)""")

def add():
    data = (int(input("Roll/ID: ")), input("Name: ").strip(),
            int(input("Age: ")), float(input("Marks: ")))
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO students VALUES (?, ?, ?, ?)", data)
    print("Student added.")

def view():
    with sqlite3.connect(DB) as con:
        rows = con.execute("SELECT * FROM students ORDER BY id").fetchall()
    for row in rows: print(row)
    if not rows: print("No records.")

def update():
    roll, marks = int(input("Roll/ID: ")), float(input("New marks: "))
    with sqlite3.connect(DB) as con:
        cur = con.execute("UPDATE students SET marks=? WHERE id=?", (marks, roll))
    print("Updated." if cur.rowcount else "Student not found.")

def delete():
    roll = int(input("Roll/ID to delete: "))
    with sqlite3.connect(DB) as con:
        cur = con.execute("DELETE FROM students WHERE id=?", (roll,))
    print("Deleted." if cur.rowcount else "Student not found.")

def main():
    setup()
    while True:
        print("\\n1.Add 2.View 3.Update marks 4.Delete 5.Exit")
        choice = input("Choice: ").strip()
        if choice == "5": break
        try:
            if choice == "1": add()
            elif choice == "2": view()
            elif choice == "3": update()
            elif choice == "4": delete()
            else: print("Choose 1-5.")
        except ValueError:
            print("Invalid numeric input.")
        except sqlite3.Error as error:
            print("Database error:", error)

if __name__ == "__main__":
    try: main()
    except sqlite3.Error as error: print("Database error:", error)
