from random import randint

lower_limit = 0
upper_limit = 9
answer = randint(lower_limit,upper_limit)
print(answer)   # TODO: Delete after testing

try_count = 1
guess = int(input("Enter a number between {} and {}: "
                  .format(lower_limit,upper_limit)))

while guess != answer:
    if try_count > 3:
        print('Exceeded attempts. Game Over.')
        break
    elif guess < answer:
        print('Guess a little higher')
    else:
        print('Guess a little lower')

    guess = int(input())
    try_count+=1
    if guess == -1:
        print('Game Over')
        break
else:
    print("You guessed it. Well done.")


