# Q30: Find the element-wise sum of two tuples
tuple1 = (10, 20, 30)
tuple2 = (1, 2, 3)
if len(tuple1) == len(tuple2):
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    print("Element-wise sum:", result)
else:
    print("Tuples must have the same length")
