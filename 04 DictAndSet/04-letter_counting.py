from string import ascii_letters, digits

word_count = {}

text = "Later in the course, you'll see how to use the collections Counter class."

for c in text.casefold():
    if c in ascii_letters or c in digits:
        word_count[c] = word_count.setdefault(c, 0) + 1

for letter, count in sorted(word_count.items()):
    print(letter, count)
