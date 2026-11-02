# Q30. Create a dictionary of characters and their frequencies.
text = input("Enter a string: ")
character_frequency = {}

for character in text:
    character_frequency[character] = character_frequency.get(character, 0) + 1

print("Character frequency dictionary:", character_frequency)
