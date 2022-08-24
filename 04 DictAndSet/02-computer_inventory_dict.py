available_parts = {
    "1": "Monitor",
    "2": "CPU",
    "3": "Mouse",
    "4": "Keyboard",
    "5": "Mouse Pad",
    "6": "HDMI Port",
    "7": "Game Pad",
    "8": "External HDD",
    "9": "Pendrive"
}

shopping_cart = []

choice = "-"
while choice != '0':
    if choice in available_parts:   # in only compares keys when used with a dictionary, not the values
        chosen_part = available_parts[choice]
        
        if chosen_part in shopping_cart:
            print(f"Removing {chosen_part}")
            shopping_cart.remove(chosen_part) # if shopping_cart were a dict, we use pop()
        else:
            print(f"Adding {chosen_part}")
            # if shopping_cart were a dict, shopping_cart[choice] = chosen_part
            shopping_cart.append(chosen_part)
        
        print(shopping_cart)
    else:
        print("Choose items for you shopping cart: ")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
        
    choice = input("> ")

print(shopping_cart)
