pangram = "the quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

print()
print(sorted(set(letters)))     # Converting to set here to remove multiple occurences of letters

names = [
    "Jessica",
    "Jacobo",
    "medici",
    "erica",
    "Modi",
    "sundara"
]
names.sort()
print()
print(names)
names.sort(key=str.casefold)
print(names)

new_list = list(pangram)    # list() function created a new list from a sequence argument and returns it
print()
print(new_list)

quickest_list = [*pangram]  # * operator works same as Kotlin list unpacking
print()
print(quickest_list)

del names[-2:]
print(names)

# Changing sizes of sequences you're iterating over while deleting or changing items is something to be careful about
