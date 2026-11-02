# Program 10: Read file content and display it in uppercase.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print(content.upper())
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
