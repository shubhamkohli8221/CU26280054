# Compare character counts, ignoring case and spaces.
a = input("Enter first string: ").lower().replace(" ", "")
b = input("Enter second string: ").lower().replace(" ", "")
if len(a) != len(b):
    print("Not anagrams")
else:
    remaining = list(b)
    is_anagram = True
    for char in a:
        if char in remaining: remaining.remove(char)
        else: is_anagram = False; break
    print("Anagrams" if is_anagram else "Not anagrams")
