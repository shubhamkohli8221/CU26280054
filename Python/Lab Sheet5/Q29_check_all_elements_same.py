# Q29: Check whether all elements in a tuple are the same
items = (7, 7, 7, 7)
if len(items) == 0 or all(item == items[0] for item in items):
    print("All elements are the same")
else:
    print("Elements are not all the same")
