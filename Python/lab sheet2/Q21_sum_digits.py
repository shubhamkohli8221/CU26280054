# Find the sum of digits of a number
number = abs(int(input("Enter a number: ")))
total = 0

while number > 0:
    total += number % 10
    number //= 10

print("Sum of digits =", total)
