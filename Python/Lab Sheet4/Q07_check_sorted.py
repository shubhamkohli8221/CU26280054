# Q7. Check whether a list of numbers is sorted in ascending order.
numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
is_sorted = True

for index in range(1, len(numbers)):
    if numbers[index] < numbers[index - 1]:
        is_sorted = False
        break

print("The list is sorted in ascending order." if is_sorted
      else "The list is not sorted in ascending order.")
