# Program 20: Merge two text files into a third file.
try:
    with open("file1.txt", "r", encoding="utf-8") as first:
        first_content = first.read()
    with open("file2.txt", "r", encoding="utf-8") as second:
        second_content = second.read()
    with open("merged.txt", "w", encoding="utf-8") as merged:
        merged.write(first_content)
        if first_content and not first_content.endswith("\\n"):
            merged.write("\\n")
        merged.write(second_content)
    print("Files merged into merged.txt.")
except FileNotFoundError as error:
    print("Required file not found:", error.filename)
