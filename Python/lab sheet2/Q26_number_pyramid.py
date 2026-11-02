# Print a pyramid pattern of numbers
for row in range(1, 6):
    print(" " * (5 - row), end="")

    for number in range(1, row + 1):
        print(number, end=" ")

    print()
