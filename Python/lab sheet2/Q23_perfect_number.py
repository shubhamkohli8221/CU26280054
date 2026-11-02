# Check whether a number is perfect
number = int(input("Enter a number: "))
total = 0

for divisor in range(1, number):
    if number % divisor == 0:
        total += divisor

if total == number:
    print("Perfect number")
else:
    print("Not a perfect number")
