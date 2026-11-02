# Program 7: Take multiple lines from the user and save them to a file.
# Enter END on a separate line when you have finished.
try:
    with open("user_notes.txt", "w", encoding="utf-8") as file:
        print("Enter text (type END to finish):")
        while True:
            line = input()
            if line == "END":
                break
            file.write(line + "\\n")
    print("Input saved to user_notes.txt.")
except OSError as error:
    print("File error:", error)
