# Q29. Find common keys between two dictionaries.
first = {"name": "Aman", "roll": 1, "marks": 82}
second = {"roll": 1, "marks": 90, "course": "MCA"}
common_keys = []

for key in first:
    if key in second:
        common_keys.append(key)

print("Common keys:", common_keys)
