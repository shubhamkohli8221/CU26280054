# Q6: Remove an element using discard()
items = {10, 20, 30, 40}
value = int(input("Enter the number to discard: "))
items.discard(value)  # No error if the value is absent.
print("Updated set:", items)
