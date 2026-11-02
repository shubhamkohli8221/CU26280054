# Program 1: Create a text file and write content into it.
try:
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("Hello! This is my first file handling program.\\n")
        file.write("Python makes file handling easy.")
    print("Content written to sample.txt successfully.")
except OSError as error:
    print("File error:", error)
