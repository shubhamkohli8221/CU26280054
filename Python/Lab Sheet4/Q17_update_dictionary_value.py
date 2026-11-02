# Q17. Update the value of a key in a dictionary.
student = {"name": "Aman", "marks": 75}
key = input("Enter key to update: ")

if key in student:
    new_value = input("Enter new value: ")
    student[key] = new_value
    print("Updated dictionary:", student)
else:
    print("Key does not exist.")
