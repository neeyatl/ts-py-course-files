choice = "-"  # initialise choice to something invalid
valid_input = set("12345")
while choice != "0":
    # if choice in "12345":     # Bug fix: 123 is in string "12345", but not in set("12345") = {'1','2','3','4','5'}
    # if choice in set("12345"):  # set is more efficient than a list or a tuple here because set uses hases.
    # if choice in {'1','2','3','4','5'}:   # Much faster/efficient over calling set() constructor
    if choice in valid_input:   # Predefined, so an object isn't created in the loop every time
        # Optimisations like these are only relevant when dealing with a huge set and your application is time-sensitive.
        # It depends on what you're working with, not always required.
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
