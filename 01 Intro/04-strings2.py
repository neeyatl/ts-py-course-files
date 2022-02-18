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