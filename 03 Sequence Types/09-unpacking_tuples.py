games = [
    ("Ruby", "GBA", 2004, [
        (1, "Treecho"),
        (4, "Torchic"),
        (7, "Mudkip"),
    ]),
    ("Sapphire", "GBA", 2004, [
        (1, "Treecho"),
        (4, "Torchic"),
        (7, "Mudkip"),
    ]),
    ("HeartGold", "NDS", 2006, [
        (1, "Chicorita"),
        (4, "Cynadaquil"),
        (7, "Totodile"),
    ]),
    ("White", "NDS", 2010, [
        (1, "Snivy"),
        (4, "Tepig"),
        (7, "Oshawatt"),
    ]),
    ("Ultra Moon", "3DS", 2010, [
        (1, "Rowlett"),
        (4, "Litten"),
        (7, "Primarina"),
    ]),
    ("Brilliant Diamond", "Switch", 2014, [
        (1, "Turtwig"),
        (4, "Chimchar"),
        (7, "Piplup"),
    ]),
    ("Sword", "Switch", 2018, [
        (1, "Grookey"),
        (4, "Scorbunny"),
        (7, "Sobble"),
    ]),
]

# for title, console, year in games:
#     print("Title: {}, Console: {}, Year: {}"
#           .format(title, console, year))

# Printing Piplup
print(games[5][3][2][1])
print()

POKEMON_LIST_INDEX = 3

choice = "-"
while choice != "q":
    if choice in "".join(str(digit) for digit in range(1, len(games) + 1)):
        pmn_choice = "-"
        print("Choose a Pokemon: ")
        pokemon = games[int(choice) - 1][POKEMON_LIST_INDEX]
        for i in range(len(pokemon)):
            print("{:3}: {}"
                  .format(i + 1, pokemon[i][1]))

        pmn_choice = input()
        if pmn_choice in "".join(str(digit) for digit in range(1, len(pokemon) + 1)):
            i_choose_you = pokemon[int(pmn_choice) - 1]
            print("Dex Number: {:3} \t {}"
                  .format(*i_choose_you))
            print()
            choice = '-'    # Resetting choice to execute the else-statement below
        
    else:
        print("Choose a game (Enter q to exit): ")
        for i, (title, console, year, pokemon) in enumerate(games):
            print("{:3}: {} ({} console) (released in {})"
                  .format(i + 1, title, console, year))

        choice = input()
        print()
print("Closing Pokedex")
print()