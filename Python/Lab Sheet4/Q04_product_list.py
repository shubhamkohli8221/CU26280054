# Q4. Find the product of all elements in a list.
numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
product = 1

for number in numbers:
    product *= number

print("Product:", product if numbers else 0)
