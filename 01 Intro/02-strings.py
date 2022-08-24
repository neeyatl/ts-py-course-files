greeting = "Sup"
print(greeting, input('Your name? ') + '?')

long_str = """
A long
long
long string for you
"""

print(greeting,long_str)

no_new_lines = """\
No \
new lines \
for \
you \
"""

print(no_new_lines)

for i in long_str.split(' '):
    print(i)
    
print(3**2)

print("A backslash \\ is printed")

print(r"A raw string \ is auto escape")

print(type(22))

print(i)