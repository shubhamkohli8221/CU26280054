# Q22: Flatten a one-level nested tuple
nested = ((1, 2), (3, 4), (5, 6))
flattened = tuple(item for sub_tuple in nested for item in sub_tuple)
print("Nested tuple:", nested)
print("Flattened tuple:", flattened)
