# Print all prime numbers between 1 and 100
for number in range(2, 101):
    prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            prime = False
            break

    if prime:
        print(number, end=" ")

print()
