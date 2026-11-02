# Q8. Find pairs of numbers whose sum equals a target.
numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
target = float(input("Enter target sum: "))
pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

if pairs:
    print("Pairs:", pairs)
else:
    print("No pairs found.")
