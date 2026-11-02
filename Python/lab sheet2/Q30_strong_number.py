# Check whether a number is a strong number
number = int(input("Enter a number: "))
original = number
total = 0

while number > 0:
    digit = number % 10
    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    total += factorial
    number //= 10

if total == original:
    print("Strong number")
else:
    print("Not a strong number")
