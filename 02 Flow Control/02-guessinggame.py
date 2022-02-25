answer = 5

guess = int(input("Enter a number between 0 and 9: "))

if guess == answer:
    print("You got it the first time.")
else:
    if guess < answer:
        print('Guess a little higher')
    else:
        print('Guess a little lower')
    guess = int(input())
    if(guess == answer):
        print("You guessed it. Well done.")
    else:
        print('You guessed incorrectly')

