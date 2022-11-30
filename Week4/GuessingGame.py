from random import randint
while True:
    level = int(input('Level: '))
    if level < 0:
        pass
    else:
        break
while True:
    guess_rand = randint(1, level)
    guess_hum = int(input('Guess: '))
    if guess_hum == guess_rand:
        print('Just right!')
        break
    elif guess_hum > guess_rand:
        print('Too large!')
    elif guess_hum < guess_rand:
        print('Too small!')
    else:
        pass