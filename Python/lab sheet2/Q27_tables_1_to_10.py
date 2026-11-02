# Display multiplication tables from 1 to 10
for number in range(1, 11):
    print("Table of", number)

    for multiplier in range(1, 11):
        print(number, "x", multiplier, "=", number * multiplier)

    print()
