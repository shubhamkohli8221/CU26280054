# Program 4: Count the number of words in a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        word_count = len(file.read().split())
    print("Number of words:", word_count)
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
