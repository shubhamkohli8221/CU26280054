# Program 14: Display the longest line in a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        longest = max(lines, key=len)
        print("Longest line:", longest.rstrip("\\n"))
        print("Length:", len(longest.rstrip("\\n")))
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
