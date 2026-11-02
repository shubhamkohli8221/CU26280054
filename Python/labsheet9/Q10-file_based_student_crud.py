# File-based CRUD using JSON for reliable structured record storage.
import json
from pathlib import Path
FILE = Path("student_records.json")
def load():
    if not FILE.exists(): return []
    return json.loads(FILE.read_text(encoding="utf-8"))
def save(records):
    FILE.write_text(json.dumps(records, indent=2), encoding="utf-8")
def add(records):
    roll = int(input("Roll number: "))
    if any(s["roll"] == roll for s in records):
        print("Roll number already exists."); return
    records.append({"roll": roll, "name": input("Name: ").strip(),
                    "age": int(input("Age: ")), "marks": float(input("Marks: "))})
    save(records); print("Record added.")
def view(records):
    for s in records: print(s)
    if not records: print("No records.")
def modify(records):
    roll = int(input("Roll number: "))
    s = next((x for x in records if x["roll"] == roll), None)
    if s:
        s["name"] = input("New name: ").strip()
        s["age"] = int(input("New age: "))
        s["marks"] = float(input("New marks: "))
        save(records); print("Record updated.")
    else: print("Record not found.")
def delete(records):
    roll = int(input("Roll number: "))
    kept = [s for s in records if s["roll"] != roll]
    if len(kept) == len(records): print("Record not found.")
    else: save(kept); print("Record deleted.")
try:
    records = load()
    while True:
        choice = input("\\n1.Add 2.View 3.Modify 4.Delete 5.Exit: ").strip()
        if choice == "1": add(records); records = load()
        elif choice == "2": view(records)
        elif choice == "3": modify(records); records = load()
        elif choice == "4": delete(records); records = load()
        elif choice == "5": break
        else: print("Invalid choice.")
except (ValueError, OSError, json.JSONDecodeError) as error:
    print("Input/file error:", error)
