# Program 11: Search for a word in a text file (case-insensitive).
try:
    target = input("Enter the word to search: ").casefold()
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().casefold().split()
    if target in words:
        print("Word found in the file.")
    else:
        print("Word not found in the file.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
