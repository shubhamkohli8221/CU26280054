# Q9. Flatten a nested list (one level of nesting).
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Nested list:", nested_list)
print("Flattened list:", flat_list)
