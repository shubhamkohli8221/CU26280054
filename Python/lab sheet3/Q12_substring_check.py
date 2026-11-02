# Check for a substring with a simple character-by-character scan.
text = input("Enter the main string: ")
sub = input("Enter the substring: ")
found = (sub == "")
for i in range(len(text) - len(sub) + 1):
    if text[i:i + len(sub)] == sub: found = True
print("Substring found" if found else "Substring not found")
