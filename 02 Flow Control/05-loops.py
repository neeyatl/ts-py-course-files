data = input('Enter numbers using any separators: ')
separators = ''

for char in data:
    if not char.isnumeric():
        separators += char

print(separators)


quote = """\
Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?
"""
for char in quote:
    if char.isupper():
        print(char)
