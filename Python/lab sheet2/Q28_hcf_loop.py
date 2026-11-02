# Find HCF of two numbers using a loop
a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))

hcf = 1
limit = min(a, b)

for divisor in range(1, limit + 1):
    if a % divisor == 0 and b % divisor == 0:
        hcf = divisor

print("HCF =", hcf)
