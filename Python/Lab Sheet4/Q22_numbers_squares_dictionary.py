# Q22. Create a dictionary with numbers as keys and squares as values.
n = int(input("Enter a positive integer n: "))

if n < 1:
    print("Please enter an integer greater than zero.")
else:
    squares = {}
    for number in range(1, n + 1):
        squares[number] = number ** 2
    print("Number-square dictionary:", squares)
