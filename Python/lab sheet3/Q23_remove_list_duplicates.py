# Preserve the first occurrence of each list value.
items = input("Enter items separated by spaces: ").split()
unique = []
for item in items:
    if item not in unique: unique.append(item)
print("Without duplicates:", unique)
