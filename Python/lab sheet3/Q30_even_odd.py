# Separate entered integers by parity.
try:
    nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
    even = []
    odd = []
    for number in nums:
        if number % 2 == 0: even.append(number)
        else: odd.append(number)
    print("Even numbers:", even)
    print("Odd numbers:", odd)
except ValueError:
    print("Please enter valid integers.")
