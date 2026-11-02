# Find LCM of two numbers using a loop
a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))

if a == 0 or b == 0:
    print("LCM = 0")
else:
    lcm = max(a, b)

    while lcm % a != 0 or lcm % b != 0:
        lcm += 1

    print("LCM =", lcm)
