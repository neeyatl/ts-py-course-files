available_parts = ["Monitor",
                   "CPU",
                   "Mouse",
                   "Keyboard",
                   "Mouse Pad",
                   "HDMI Port",
                   "Game Pad",
                   "External HDD",
                   "Pendrive"
                   ]
current_choice = "-1"  # Initialized with an unreachable value to ensure compatability
computer_parts = []

while current_choice != '0':
    if int(current_choice) in range(len(available_parts)+1):
        if available_parts[int(current_choice) - 1] in computer_parts:
            print("Removing item {}".format(current_choice))
            computer_parts.remove(available_parts[int(current_choice) - 1])     # remove(x) method removed item x from list if it exists or throws ValueError
        else:
            print("Adding item {}".format(current_choice))
            computer_parts.append(available_parts[int(current_choice) - 1])
        print(computer_parts)
        
    else:
        for num, part in enumerate(available_parts):    # enumerate function works like Kotlin method withIndex()
            print("{}: {}".format(num + 1, part))
        
        print("0: To Finish")
        
    current_choice = input()
    
print(computer_parts)