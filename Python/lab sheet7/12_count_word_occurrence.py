# Program 12: Count how many times a word occurs in a text file.
import re

try:
    target = input("Enter the word to count: ")
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    occurrences = len(re.findall(r"\\b" + re.escape(target) + r"\\b", content, re.IGNORECASE))
    print("Occurrences:", occurrences)
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
