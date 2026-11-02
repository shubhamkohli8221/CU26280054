# Q5. Create a list of squares of numbers from 1 to n.
n = int(input("Enter a non-negative integer n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    squares = [number ** 2 for number in range(1, n + 1)]
    print("Squares:", squares)
