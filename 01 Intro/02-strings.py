greeting = "Sup"
print(greeting, input('Your name? ') + '?')

long_str = """
A long
long
long string for you
"""

print(greeting,long_str)

not_split = """\
No \
new lines \
for \
you
"""

print(not_split)

for i in long_str.split(' '):
    print(i)
    
print(3**2)

print("A backslash \\ is printed")

print(r"A raw string \ is auto escape")

print(type(22))

print(i)