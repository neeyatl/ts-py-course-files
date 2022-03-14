numbers = [
    101, 23, 12, 231, 45, 99, 102, 302, 14, 291, 123, 90
]

min_val = 100
max_val = 200

# for i in range(len(numbers) - 1, -1, -1):
#     if not min_val < numbers[i] < max_val:
#         del numbers[i]

top_i = len(numbers) - 1
for i, num in enumerate(reversed(numbers)): # more efficient compared to above method
    if not min_val < num < max_val:
        print("{:2}\t{:3}".format(i,num))
        del numbers[top_i - i]

print(numbers)