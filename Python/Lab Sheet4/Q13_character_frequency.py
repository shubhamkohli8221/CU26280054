# Q13. Count character frequency using a dictionary.
text = input("Enter a string: ")
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print("Character frequencies:", frequency)
