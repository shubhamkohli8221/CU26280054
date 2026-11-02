# Reverse list order using a loop, without reversed() or slicing.
items = input("Enter items separated by spaces: ").split()
result = []
i = len(items) - 1
while i >= 0:
    result.append(items[i])
    i -= 1
print("Reversed:", result)
