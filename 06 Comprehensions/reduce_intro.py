from functools import reduce


def mulit(x, y):
    return x * y


numbers = range(1, 12)

print(reduce(mulit, numbers))

product = 1
for n in numbers:
    product *= n

print(product)
