# Q3. Remove all negative numbers from a list.
numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
non_negative = [number for number in numbers if number >= 0]
print("List after removing negative numbers:", non_negative)
