# Q16. Sort a dictionary by values (ascending).
data = {"Aman": 78, "Riya": 91, "Karan": 65}
sorted_items = sorted(data.items(), key=lambda item: item[1])
sorted_data = dict(sorted_items)
print("Sorted by values:", sorted_data)
