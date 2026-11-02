# Print every non-empty contiguous substring.
text = input("Enter a string: ")
for start in range(len(text)):
    for end in range(start + 1, len(text) + 1):
        print(text[start:end])
