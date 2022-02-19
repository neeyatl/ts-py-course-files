parrot = 'Norwegian Blue'

print(parrot)
print()

for i in range(3,5):
    print(parrot[i])

print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()

print(parrot[::-1])
print()

print(parrot[-1])   #Prints last char from str. Counting backwards from -1 since -0 doesn't exist in Python.
print(parrot[-14])
print()


print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()

# index - length gives the exact negative indexing values
len = 14
print(parrot[3 - len])
print(parrot[4 - len])
print(parrot[9 - len])
print(parrot[3 - len])
print(parrot[6 - len])
print(parrot[8 - len])
print()

print(parrot[0:3])
print(parrot[3:5])
print(parrot[:3])   # Start value defaults to the beginning index
print(parrot[10:])  # End value defaults to length
print()
print(parrot[:6] + parrot[6:])
print()
print(parrot[:])
print(parrot[::2])
print(parrot[::1])
# print(parrot[::0])  # ValueError: slice step cannot be zero

print('\n')

print(parrot[-4:2:-1])  # -4 => B and not including 2 => r


number = '198;232 145 168:192,343;903'
separators = number[3::4]
print(separators)

values = "".join(c if c not in separators else " " for c in number).split()
print(values)
print([int(num) for num in values]) # Generate a list of integers