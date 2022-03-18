small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(12)
small_ints.remove(13)
print(small_ints)

small_ints.discard(99)  # No error if item doesn't exist
print(small_ints)

small_ints.remove(99)   # Throws an error if item doesn't exist
print(small_ints)