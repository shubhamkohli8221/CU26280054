# Print distinct values that appear in both lists, in first-list order.
a = input("Enter first list items separated by spaces: ").split()
b = input("Enter second list items separated by spaces: ").split()
common = []
for item in a:
    if item in b and item not in common: common.append(item)
print("Common elements:", common)
