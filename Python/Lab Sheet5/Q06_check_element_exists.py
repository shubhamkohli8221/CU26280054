# Q6: Check whether an element exists in a tuple
items = (10, 20, 30, 40, 50)
value = int(input("Enter a number to search: "))
if value in items:
    print(value, "exists in the tuple")
else:
    print(value, "does not exist in the tuple")
