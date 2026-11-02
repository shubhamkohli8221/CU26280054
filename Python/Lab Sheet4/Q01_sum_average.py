# Q1. Find the sum and average of elements in a list.
numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print("List:", numbers)
    print("Sum:", total)
    print("Average:", average)
else:
    print("Please enter at least one number.")
