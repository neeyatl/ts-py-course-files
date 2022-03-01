available_exits = ['north', 'south', 'east', 'west']
chosen_exit = ''

while chosen_exit not in available_exits:
    chosen_exit = input('Choose a valid exit to get out: ')
    if chosen_exit.casefold() == 'quit':
        print('Game Over')
        break

print("It's good to finally get some fresh air, isn't it?")