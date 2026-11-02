# Q27. Remove duplicate values from a dictionary, keeping the first key.
data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
unique_data = {}
seen_values = []

for key, value in data.items():
    if value not in seen_values:
        unique_data[key] = value
        seen_values.append(value)

print("Original dictionary:", data)
print("Without duplicate values:", unique_data)
