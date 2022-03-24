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

for meal in[[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)