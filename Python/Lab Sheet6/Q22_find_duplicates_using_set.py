# Q22: Find duplicate elements in a list using a set
items = input("Enter elements separated by spaces: ").split()
seen = set()
duplicates = set()

for item in items:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicate elements:", duplicates)
