import random

def game():
    choices = ['rock', 'paper', 'scissors']
    beats = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    }
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper or scissors?: ').lower()

    print('computer: ', computer)
    print('player: ', player)

    if player == computer:
        print('Tie!')
    elif beats[player] == computer:
        print('You win!')
    else:
        print('You loose!')



while True:
    game()

    if input("Play again? (yes/no): ").lower() != 'yes':
        break

print('Bye!')