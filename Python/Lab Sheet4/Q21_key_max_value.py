# Q21. Find the key with the maximum value without max().
data = {"A": 25, "B": 48, "C": 36}

if data:
    iterator = iter(data.items())
    largest_key, largest_value = next(iterator)

    for key, value in iterator:
        if value > largest_value:
            largest_key, largest_value = key, value

    print("Key with maximum value:", largest_key)
    print("Maximum value:", largest_value)
else:
    print("Dictionary is empty.")
