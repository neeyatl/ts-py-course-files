# immutable type str
name = 'Subhas Chandra Bose'
another_name = name
print(id(name))
print(id(another_name))

prefix = "Netaji "
name = prefix + name
print(name)
print(id(name))

print()

# mutable type list
snacks = ['chips', 'noodles', 'dates', 'almonds']
snacks2 = snacks
print(id(snacks))
print(id(snacks2))

snacks += ['peanuts', 'omlet']
print(snacks)
print(id(snacks))
