# Collect uppercase letters from the input.
text = input("Enter a string: ")
result = ""
for char in text:
    if char.isupper(): result += char
print("Uppercase characters:", result)
