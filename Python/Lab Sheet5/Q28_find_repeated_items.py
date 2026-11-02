# Q28: Find repeated items in a tuple (each repeated value shown once)
items = (1, 2, 3, 2, 4, 1, 5, 3, 3)
repeated_values = []

# Keep each value once if it occurs more than one time.
for item in items:
    if items.count(item) > 1 and item not in repeated_values:
        repeated_values.append(item)

print("Repeated items:", tuple(repeated_values))
