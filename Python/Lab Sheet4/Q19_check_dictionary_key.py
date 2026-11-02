# Q19. Check whether a key exists in a dictionary.
student = {"name": "Aman", "roll": 12, "marks": 75}
key = input("Enter key to search for: ")

if key in student:
    print("Key exists. Value:", student[key])
else:
    print("Key does not exist.")
