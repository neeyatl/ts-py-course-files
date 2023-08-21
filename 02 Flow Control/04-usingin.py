activity = input('Enter your preferred activity: ')

if 'trekking' not in activity.casefold():   # casefold is aggressive lowercase
    print('But I wanna go trekking.')
else: print("That's a healthy choice.")
