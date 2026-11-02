# Program 16: Display the first and last lines of a file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        print("First line:", lines[0].rstrip("\\n"))
        print("Last line:", lines[-1].rstrip("\\n"))
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
