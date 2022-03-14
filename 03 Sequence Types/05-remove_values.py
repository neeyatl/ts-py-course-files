numbers = [
    30, 38, 102, 109, 119, 123, 176, 189, 183, 198, 199, 201, 262
]

min_val = 100
max_val = 200

# This code is much more efficient than reversed list methods.
# Deleting a slice is efficient over deleting individual items.
# trim smaller values
stop = None
for i, num in enumerate(numbers):
    if num >= min_val:
        stop = i
        break

if stop is not None:
    del numbers[:stop]
print(numbers)

# trim larger values
start = None
for i in range(len(numbers) - 1,-1,-1):
    if numbers[i] <= max_val:
        start = i + 1   # + 1 because we want to include the max_val or any value less than max_val
        break

if start is not None:
    del numbers[start:]
print(numbers)
