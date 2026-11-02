# Q24: Find common elements between two tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7)
common = tuple(item for item in tuple1 if item in tuple2)
print("Common elements:", common)
