# Q27: Unzip a list of tuples into individual lists
pairs = [(1, "A"), (2, "B"), (3, "C")]
numbers, letters = zip(*pairs)
print("Numbers:", list(numbers))
print("Letters:", list(letters))
