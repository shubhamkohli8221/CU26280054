# Q4: Add multiple elements to a set
items = {10, 20, 30}
values = input("Enter elements separated by spaces: ").split()
items.update(values)
print("Updated set:", items)
