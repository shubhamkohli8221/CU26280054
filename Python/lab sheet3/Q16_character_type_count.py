# Count digits, alphabetic characters, and remaining characters.
text = input("Enter a string: ")
digits = alphabets = special = 0
for char in text:
    if char.isdigit(): digits += 1
    elif char.isalpha(): alphabets += 1
    else: special += 1
print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special characters (including spaces):", special)
