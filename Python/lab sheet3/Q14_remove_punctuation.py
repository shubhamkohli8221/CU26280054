# Remove standard punctuation marks.
import string
text = input("Enter a string: ")
result = ""
for char in text:
    if char not in string.punctuation: result += char
print(result)
