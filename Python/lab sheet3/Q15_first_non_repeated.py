# Print the first character that occurs exactly once.
text = input("Enter a string: ")
for char in text:
    count = 0
    for other in text:
        if char == other: count += 1
    if count == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found.")
