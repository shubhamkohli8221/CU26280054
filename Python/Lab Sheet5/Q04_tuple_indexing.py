# Q4: Access tuple elements using indexing
items = ("red", "green", "blue", "yellow")
index = int(input("Enter an index (0 to 3): "))
if 0 <= index < len(items):
    print("Element:", items[index])
else:
    print("Invalid index")
