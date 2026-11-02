# Check whether the entered text reads the same forwards and backwards.
text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Palindrome" if text == reversed_text else "Not a palindrome")
