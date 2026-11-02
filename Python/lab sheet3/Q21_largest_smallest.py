# Find minimum and maximum values in a list of integers.
try:
    nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
    if not nums: print("Please enter at least one integer.")
    else:
        smallest = largest = nums[0]
        for number in nums[1:]:
            if number < smallest: smallest = number
            if number > largest: largest = number
        print("Smallest:", smallest)
        print("Largest:", largest)
except ValueError:
    print("Please enter valid integers.")
