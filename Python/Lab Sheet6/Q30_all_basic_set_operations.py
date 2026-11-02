# Q30: Perform union, intersection, difference, and symmetric difference
set1 = set(map(int, input("Enter numbers for set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter numbers for set 2 separated by spaces: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric difference:", set1 ^ set2)
