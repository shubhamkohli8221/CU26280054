# Q25: Find common letters in two strings using sets
text1 = input("Enter the first string: ").lower()
text2 = input("Enter the second string: ").lower()
letters1 = set(text1)
letters2 = set(text2)
common = (letters1 & letters2) - {" "}
print("Common characters:", common)
