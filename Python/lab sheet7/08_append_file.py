# Program 8: Append new content without deleting existing content.
try:
    new_text = input("Enter text to append: ")
    with open("sample.txt", "a", encoding="utf-8") as file:
        file.write("\\n" + new_text)
    print("Content appended successfully.")
except OSError as error:
    print("File error:", error)
