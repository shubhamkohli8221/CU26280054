# Sort the given integers in both directions.
try:
    nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
    print("Ascending:", sorted(nums))
    print("Descending:", sorted(nums, reverse=True))
except ValueError:
    print("Please enter valid integers.")
