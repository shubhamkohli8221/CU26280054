# Q23: Remove duplicates from a list using a set
items = input("Enter elements separated by spaces: ").split()
unique_items = list(set(items))
print("List without duplicates (order may change):", unique_items)
