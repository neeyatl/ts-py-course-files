entries = [n for n in range(1,6)]

print(f"All: {all(entries)}")
print(f"Any: {any(entries)}")
print()

# Any empty iterable, None, False or zero values are False in Python
entries[2] = 0
print(f"All: {all(entries)}")   # All entries are not true, so it'll return False
print(f"Any: {any(entries)}")   # As long as any value in entries is true, it returns True
print()

entries.clear()
print(f"All: {all(entries)}")   # all() returns True when list is empty which may be unwanted
print(f"Any: {any(entries)}")   # any() is fine
print()

print(f"All: {bool(entries) and all(entries)}")     # When this test is applied, the above conundrum is resolved
print(f"Any: {any(entries)}")
print()