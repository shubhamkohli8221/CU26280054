# Keep only each character's first occurrence.
text = input("Enter a string: ")
result = ""
for char in text:
    if char not in result: result += char
print("Without duplicates:", result)
