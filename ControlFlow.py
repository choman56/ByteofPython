number = 23

guess = int(input('Enter a whole number: '))

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

print('Done')