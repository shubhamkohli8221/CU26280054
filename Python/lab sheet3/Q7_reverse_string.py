# Reverse a string by reading its characters from the end.
text = input("Enter a string: ")
result = ""
i = len(text) - 1
while i >= 0:
    result += text[i]
    i -= 1
print("Reversed:", result)
