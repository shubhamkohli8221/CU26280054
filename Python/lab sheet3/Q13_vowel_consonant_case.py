# Uppercase vowels and lowercase consonants; preserve other characters.
text = input("Enter a string: ")
result = ""
for char in text:
    if char.lower() in "aeiou": result += char.upper()
    elif char.isalpha(): result += char.lower()
    else: result += char
print(result)
