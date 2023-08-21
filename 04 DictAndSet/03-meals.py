from contents import pantry, recipes

display_dict = {str(i + 1): meal for i, meal in enumerate(recipes)}
print(display_dict)

shopping_pantry = {}

def add_to_dict(data: dict, item: str, quantity: int):
    # if item in data:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity
    data[item] = data.setdefault(item, 0) + quantity

choice = "-"
while choice != '0':
    if choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You selected {selected_item}")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients,"\n")
        for food_item, req_quantity in ingredients.items():
            available_quantity = pantry.get(food_item, 0)   # indexing will give an error. If no item, defaut value is 0 through get()
            if req_quantity <= available_quantity:
                print(f"\t{food_item} Available")
            else:
                purchase_quantity = req_quantity - available_quantity
                print(f"\tNeed to buy {purchase_quantity} of {food_item}")
                add_to_dict(shopping_pantry, food_item, purchase_quantity)
                
        print(f"Your shopping list now: {shopping_pantry}")
    else:
        print("Choose a meal: ")
        for key, value in display_dict.items():
            print(f"{key} - {value}")
        print("0: to finish")
        
    choice = input("> ")

print("\nYour shopping list: ")

for item in shopping_pantry.items():
    print(item)

print()
