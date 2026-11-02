# Check whether a number is a palindrome
number = input("Enter a number: ")

if number == number[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
