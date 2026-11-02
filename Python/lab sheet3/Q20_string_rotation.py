# Check whether the second string is a rotation of the first.
a = input("Enter first string: ")
b = input("Enter second string: ")
if len(a) == len(b) and b in (a + a):
    print("Rotations")
else:
    print("Not rotations")
