# Count occurrences of each character, including spaces.
text = input("Enter a string: ")
seen = ""
for char in text:
    if char not in seen:
        count = 0
        for other in text:
            if other == char: count += 1
        print(repr(char) + ":", count)
        seen += char
