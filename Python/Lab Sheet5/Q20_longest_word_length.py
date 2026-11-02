# Q20: Find the length of the longest word in a tuple
words = ("cat", "elephant", "tiger", "butterfly")
if words:
    longest_length = max(len(word) for word in words)
    print("Length of the longest word:", longest_length)
else:
    print("Tuple is empty")
