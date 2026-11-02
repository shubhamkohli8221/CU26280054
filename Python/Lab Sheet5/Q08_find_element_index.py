# Q8: Find the index of an element in a tuple
items = (10, 20, 30, 20, 40)
value = int(input("Enter a number to find: "))
if value in items:
    print("First index:", items.index(value))
else:
    print("Element not found")
