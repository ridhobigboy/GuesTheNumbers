import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess < random_number:
            print('Sorry, guess again. Too low')    
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    print(f'yay, congrats, you have guessed he number. {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'is {guess} too high (H), to low (L), or correct(C)??'). lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'L':
            low = guess + 1
    print (f'yeay, the computer guess your number , {guess}, correctly')

computer_guess(50)