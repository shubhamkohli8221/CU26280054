# Q28: Create a frozenset and demonstrate its properties
items = frozenset({10, 20, 30})
print("Frozen set:", items)
print("Contains 20:", 20 in items)
print("Length:", len(items))

# A frozenset is immutable; adding or removing elements is not allowed.
print("Union with {30, 40}:", items | {30, 40})
