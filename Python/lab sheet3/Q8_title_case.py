# Capitalize the first letter of each word without title().
text = input("Enter a string: ")
result = ""
new_word = True
for char in text:
    if char.isspace():
        result += char
        new_word = True
    elif new_word:
        result += char.upper()
        new_word = False
    else:
        result += char.lower()
print(result)
