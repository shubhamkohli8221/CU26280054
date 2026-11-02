# Check whether a number is an Armstrong number
number = input("Enter a number: ")
power = len(number)
total = 0

for digit in number:
    total += int(digit) ** power

if total == int(number):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
