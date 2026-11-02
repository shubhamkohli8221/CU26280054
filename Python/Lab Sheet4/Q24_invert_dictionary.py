# Q24. Invert a dictionary (values become keys).
data = {"Aman": 1, "Riya": 2, "Karan": 3}
inverted = {}

for key, value in data.items():
    if value in inverted:
        print("Warning: duplicate values mean an earlier key may be overwritten.")
    inverted[value] = key

print("Original dictionary:", data)
print("Inverted dictionary:", inverted)
