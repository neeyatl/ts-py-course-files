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

# for when: numbers = [102, 109, 119, 123, 176, 189, 183, 198, 199]
print([i for i in range(len(numbers) - 1,-1,-1)])
# [8, 7, 6, 5, 4, 3, 2, 1, 0]
print([i for i in range(len(numbers) - 1,0,-1)])
# [8, 7, 6, 5, 4, 3, 2, 1]
print([i for i in range(0,-1,-1)])
# [0]
print([i for i in range(-1,0,-1)])
# []
print([i for i in range(-1,-1,-1)])
# []
print([i for i in range(10,11,-1)])
# []

'''From above outputs, we see that -1 value as start or stop indicates position before 0 
which is non-existent. When -1 is being accessed, the result is empty. 
It's use is to include 0 index during reverse traversal. As can be seen in second case, 
use of zero as stop value omits 0th index because range is upto but not including the stop value.'''
