from string import ascii_letters, digits

char_count = {}

text = "Later in the course, you'll see how to use the collections Counter class."

for c in text.casefold():
    if c in ascii_letters or c in digits:
        char_count[c] = char_count.setdefault(c, 0) + 1

for letter, count in sorted(char_count.items()):
    print(letter, count)
