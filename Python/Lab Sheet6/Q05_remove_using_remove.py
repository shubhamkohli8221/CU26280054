# Q5: Remove an element using remove()
items = {10, 20, 30, 40}
value = int(input("Enter the number to remove: "))
try:
    items.remove(value)
    print("Updated set:", items)
except KeyError:
    print("Element was not found in the set.")
