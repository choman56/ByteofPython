number = 23
guess = 0
loopcount = 5

print('\nLet\'s play, guess the number!!\n')

while number != guess:
    if guess == 0:
        guess = int(input('Enter a whole number (-1 to bypass the guessing game): '))
    else:
        guess = int(input('Try again: '))

#    print('Guess is', guess)
    if guess == -1:
        print('I get it. You want to move on!')
        break

    if guess == number:
        # success in guessing
        print('You guessed it! Must be a mind reader.')
    elif guess < number:
        print('Too low')
        if guess - number > -5:
            print('Off by less than 5')
        elif guess - number <= -5:
            print('Off by a mile (more than 5)')
    else:
        print('Close but too high')
    loopcount -= 1
    if loopcount <= 0:
        print('Too many tries, times up!')
        break

# print('While loop is done')
print('')
stuff = 0

response = (input("Let's loop around, ok? "))
if (response == 'Y') | (response == 'y') | (response == 'Yes') | (response == 'yes') | (response == 'Yes'):
#if response == 'Y':
    for loopcount in range(0, 25, 2):
        stuff += loopcount
        print('Loop count:', loopcount, 'Stuff:', stuff)
else:
    print('I quit.')
print('')
print ('Goodbye')