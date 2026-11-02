# Q19: Create the power set of a given set
from itertools import combinations

items = {1, 2, 3}
power_set = set()
elements = list(items)

for size in range(len(elements) + 1):
    for group in combinations(elements, size):
        power_set.add(frozenset(group))

print("Power set:")
for subset in power_set:
    print(set(subset))
