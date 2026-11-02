# Q2. Rotate a list by n positions (right rotation).
items = input("Enter list items separated by spaces: ").split()
n = int(input("Enter number of positions to rotate right: "))

if items:
    n %= len(items)
    rotated = items[-n:] + items[:-n] if n else items[:]
    print("Rotated list:", rotated)
else:
    print("The list is empty.")
