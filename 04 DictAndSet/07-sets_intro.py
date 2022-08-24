farm_animals = {'goat', 'sheep', 'cow', 'hen', 'pig'}
print(farm_animals)

# number_set = {*""}
# number_set = {*{}}
number_set = set()  # less efficient, but only relevant for highly time-sensitive applications
print(number_set,type(number_set))

while len(number_set) < 4:
    next_num = int(input("Please enter next integer input: "))
    number_set.add(next_num)

print(number_set)

data = ['apple', 'tangerine', 'apple', 'bananas', 'grapes', 'tangerine', 'bananas', 'grapes']
# remove duplicates
unique_data = set(data)
print()
print(unique_data)
# sorted
sorted_unique_data = sorted(unique_data)
print(sorted_unique_data)
# preserve order of appearance
ordered_unique_data = tuple(dict.fromkeys(data))
print(ordered_unique_data)
