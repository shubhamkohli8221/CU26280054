# Display grade based on marks
marks = float(input("Enter marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks < 90:
    print("Grade: B")
elif 50 <= marks < 75:
    print("Grade: C")
elif 0 <= marks < 50:
    print("Grade: F")
else:
    print("Invalid marks.")
