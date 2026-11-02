# Find the second-largest distinct integer.
try:
    nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
    largest = second = None
    for number in nums:
        if largest is None or number > largest:
            if number != largest: second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    if second is None: print("A second distinct largest number does not exist.")
    else: print("Second largest:", second)
except ValueError:
    print("Please enter valid integers.")
