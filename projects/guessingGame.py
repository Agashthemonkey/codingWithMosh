secret_number = 7
Guessing_chances = 0
guess_limit = 3
while Guessing_chances < guess_limit:
    guess = int(input('Guess: '))
    guess_limit += 1 
    if guess == secret_number:
        print('you won! ')
        break
else:
    print('you lost!')



