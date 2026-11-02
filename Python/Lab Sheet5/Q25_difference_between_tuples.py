# Q25: Find elements in the first tuple that are not in the second
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 6)
difference = tuple(item for item in tuple1 if item not in tuple2)
print("Difference (first tuple minus second):", difference)
