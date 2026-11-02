# Print items present in the first list but absent from the second.
a = input("Enter first list items separated by spaces: ").split()
b = input("Enter second list items separated by spaces: ").split()
difference = []
for item in a:
    if item not in b and item not in difference: difference.append(item)
print("First list minus second:", difference)
