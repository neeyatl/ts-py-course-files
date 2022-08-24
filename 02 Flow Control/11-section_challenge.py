options = ['Trekking', 'Cricket Match', 'Netflix \'n chill', 'Movies', 'Date']
message = ['Lets break a sweat', 'Sixes & Fours!', 'Top 10 Trending series', "What's new in theatres?", 
           'Take her somewhere nice.']

choice = None
while choice != '0':
    for item in options:
        print('Enter {} for {}'.format(options.index(item) + 1,item))
    print('Enter 0 to exit \n')
    choice = input()
    
    if int(choice) <= len(options) and int(choice) != 0:
        print(message[int(choice)-1])
        print()
