# Program 17: Remove blank lines from a file and rewrite the file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.writelines(line for line in lines if line.strip())
    print("Blank lines removed.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_write_file.py first.")
