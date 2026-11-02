# Q12. Find maximum and minimum marks in a dictionary without max()/min().
marks = {"Aman": 78, "Riya": 91, "Karan": 65}

if marks:
    names = list(marks.keys())
    highest_name = lowest_name = names[0]
    highest = lowest = marks[names[0]]

    for name, score in marks.items():
        if score > highest:
            highest, highest_name = score, name
        if score < lowest:
            lowest, lowest_name = score, name

    print("Marks:", marks)
    print(f"Maximum: {highest} ({highest_name})")
    print(f"Minimum: {lowest} ({lowest_name})")
else:
    print("Dictionary is empty.")
