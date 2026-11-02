# Find the factorial of a number
n = int(input("Enter n: "))
factorial = 1

for number in range(1, n + 1):
    factorial *= number

print("Factorial =", factorial)
