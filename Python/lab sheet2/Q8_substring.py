# Check whether a string contains a substring
text = input("Enter the string: ")
substring = input("Enter the substring: ")

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")
