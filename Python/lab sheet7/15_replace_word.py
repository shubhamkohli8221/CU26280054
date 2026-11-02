# Program 15: Replace one word with another and save the changes to the same file.
try:
    old_word = input("Word to replace: ")
    new_word = input("Replace it with: ")
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("Replacement completed.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
