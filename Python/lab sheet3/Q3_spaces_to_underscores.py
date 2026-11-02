# Replace every space with an underscore.
text = input("Enter a string: ")
result = ""
for char in text:
    result += "_" if char == " " else char
print(result)
