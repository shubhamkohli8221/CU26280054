# Q8: Check whether an element exists in a set
items = {10, 20, 30, 40}
value = int(input("Enter a number to search for: "))
if value in items:
    print(value, "exists in the set")
else:
    print(value, "does not exist in the set")
