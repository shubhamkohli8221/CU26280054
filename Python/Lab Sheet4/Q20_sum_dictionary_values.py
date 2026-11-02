# Q20. Find the sum of all values in a dictionary.
marks = {"Aman": 78, "Riya": 91, "Karan": 65}
total = 0

for value in marks.values():
    total += value

print("Dictionary:", marks)
print("Sum of values:", total)
