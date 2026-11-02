# Sort characters alphabetically (case-insensitive key).
text = input("Enter a string: ")
chars = list(text)
chars.sort(key=str.lower)
print("".join(chars))
