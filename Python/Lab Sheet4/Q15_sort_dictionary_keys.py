# Q15. Sort a dictionary by keys.
data = {"banana": 3, "apple": 5, "cherry": 2}
sorted_data = {}

for key in sorted(data):
    sorted_data[key] = data[key]

print("Sorted by keys:", sorted_data)
