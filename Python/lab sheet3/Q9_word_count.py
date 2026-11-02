# Count words separated by whitespace.
text = input("Enter a string: ")
count = 0
in_word = False
for char in text:
    if char.isspace(): in_word = False
    elif not in_word:
        count += 1
        in_word = True
print("Word count:", count)
