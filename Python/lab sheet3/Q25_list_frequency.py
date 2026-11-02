# Show the count of each entered item.
items = input("Enter items separated by spaces: ").split()
for item in items:
    if item not in items[:items.index(item)]:
        print(item + ":", items.count(item))
