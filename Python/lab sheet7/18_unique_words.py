# Program 18: Save unique words from a text file to another file.
import re

try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = re.findall(r"\\b[\\w']+\\b", file.read().casefold())
    unique_words = sorted(set(words))
    with open("unique_words.txt", "w", encoding="utf-8") as file:
        file.write("\\n".join(unique_words))
    print("Unique words saved to unique_words.txt.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
