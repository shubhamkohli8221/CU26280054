# Count vowels and alphabetic consonants.
text = input("Enter a string: ")
vowels = consonants = 0
for char in text.lower():
    if char.isalpha():
        if char in "aeiou": vowels += 1
        else: consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
