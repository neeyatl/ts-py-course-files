burgers = ['beef', 'chicken', 'potato']
toppings = ['cheese', 'mayo', 'bacon']

for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

print()

# meals2 = []
# for burger in burgers:
#     for topping in toppings:
#         meals2.append((burger, topping))
# print(meals2)

# Nested comprehensions are faster than nested loops. Generally, comprehensions are faster than loops.
# Comprehensions are easier to read and also perform way better than map() and filter() functions.
for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)
