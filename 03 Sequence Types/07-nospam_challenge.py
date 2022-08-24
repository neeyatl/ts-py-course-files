menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

print("Printing Method")
print('-'*30)
for meal in menu:
    print(", ".join(item for item in meal if item != "spam"))

print()

print("Remove Items Method")
print('-'*30)
for meal in menu:
    top_i = len(meal) - 1
    for i, item in enumerate(reversed(meal)):
        if item == "spam":
            del meal[top_i - i]

for meal in menu:
    for item in meal:
        print(item, end=" ")
    print()
