# Perform Create, Read, Update and Delete on employee dictionary.
employees = {}
def create():
    emp_id = input("Employee ID: ").strip()
    employees[emp_id] = {"name": input("Name: ").strip(),
                         "department": input("Department: ").strip(),
                         "salary": float(input("Salary: "))}
    print("Employee saved.")
def read():
    print(employees if employees else "No employees.")
def update():
    emp_id = input("Employee ID: ").strip()
    if emp_id not in employees:
        print("Employee not found.")
        return
    employees[emp_id]["salary"] = float(input("New salary: "))
    print("Employee updated.")
def delete():
    emp_id = input("Employee ID: ").strip()
    print("Deleted." if employees.pop(emp_id, None) is not None else "Employee not found.")
try:
    while True:
        choice = input("\\n1.Create 2.Read 3.Update salary 4.Delete 5.Exit: ").strip()
        if choice == "1": create()
        elif choice == "2": read()
        elif choice == "3": update()
        elif choice == "4": delete()
        elif choice == "5": break
        else: print("Invalid choice.")
except ValueError:
    print("Salary must be numeric.")
