# Q10: Repeat a tuple n times
items = ("Python", "Tuple")
n = int(input("Enter number of repetitions: "))
if n >= 0:
    print("Repeated tuple:", items * n)
else:
    print("Please enter a non-negative number")
