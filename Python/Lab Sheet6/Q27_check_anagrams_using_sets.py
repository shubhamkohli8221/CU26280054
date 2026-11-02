# Q27: Check whether two strings are anagrams using sets
# This checks character membership; sets alone do not count repeated letters.
text1 = input("Enter the first string: ").replace(" ", "").lower()
text2 = input("Enter the second string: ").replace(" ", "").lower()

if len(text1) == len(text2) and set(text1) == set(text2):
    print("The strings have the same character set and length.")
    print("Note: to verify anagrams correctly with repeated letters, compare sorted strings.")
    print("Anagrams:", sorted(text1) == sorted(text2))
else:
    print("The strings are not anagrams.")
