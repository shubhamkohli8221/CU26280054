# Q18: Remove all elements of one set from another set
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6}
set1.difference_update(set2)
print("Updated first set:", set1)
