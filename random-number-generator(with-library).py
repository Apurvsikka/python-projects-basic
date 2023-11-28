import random as ram # importing random library

points = 0 # initializing points
# asking user to select range ot the number
print('-----------------------------Random Number Generator-----------------------------')
print('select range of the number')
lower_limit = int(input('enter lower limit: '))
upper_limit = int(input('enter upper limit: '))

# generating random number
random_number = ram.randint(lower_limit, upper_limit)

#asking user to guess the number
print('guess the number')
guess = int(input('enter your guess: '))
while guess != random_number:
    if guess < random_number:
        print('your guess is too low')
        print("as this is your first guess, you will not lose any points")
        print("your points: ", points)
    else:
        print('your guess is too high')
    guess = int(input('enter your guess: '))
print('congratulations you guessed the number correctly')
     #add points for guessing the number correctly
points +=1
print("your points: ", points)

# asking user to play again
answer = input('do you want to play again?[y/n]: ')
while answer == 'y':
    # generating random number
    lower_limit = int(input('enter lower limit: '))
    upper_limit = int(input('enter upper limit: '))
    random_number = ram.randint(lower_limit, upper_limit)

    #asking user to guess the number
    print('guess the number')
    guess = int(input('enter your guess: '))
    while guess != random_number:
        if guess < random_number:
            print('your guess is too low')
            points -= 1
            print("your points: ", points)
        else:
            print('your guess is too high')
            points -= 1
            print("your points: ", points)
        guess = int(input('enter your guess: '))
    print('congratulations you guessed the number correctly')
     #add points for guessing the number correctly
    points += 1
    print("your points: ", points)

    print('do you want to play again?[y/n]')
    answer = input('enter your answer: ')














# made by github.com/Apurvsikka