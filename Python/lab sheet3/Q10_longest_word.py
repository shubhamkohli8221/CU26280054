# Find a longest whitespace-separated word.
words = input("Enter a string: ").split()
if words:
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest): longest = word
    print("Longest word:", longest)
else:
    print("No words entered.")
