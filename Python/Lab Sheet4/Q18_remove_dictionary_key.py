# Q18. Remove a key from a dictionary.
student = {"name": "Aman", "roll": 12, "marks": 75}
key = input("Enter key to remove: ")

if key in student:
    del student[key]
    print("Updated dictionary:", student)
else:
    print("Key does not exist.")
