# Program 9: Copy the content of one text file to another.
source_file = "sample.txt"
destination_file = "sample_copy.txt"

try:
    with open(source_file, "r", encoding="utf-8") as source:
        content = source.read()
    with open(destination_file, "w", encoding="utf-8") as destination:
        destination.write(content)
    print("Content copied to", destination_file)
except FileNotFoundError:
    print(source_file, "was not found.")
except OSError as error:
    print("File error:", error)
