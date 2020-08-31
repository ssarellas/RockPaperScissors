#rock paper scissors game

import random

option = ['rock', 'paper', 'scissors']

computer = option[random.randint(0,2)]

player = False

while player == False:
    player = input('Rock, Paper or Scissors?\n')
    if player.lower() == computer:
        print('Tie!')
    elif player.lower() == 'rock':
        if computer.lower() == 'paper':
            print('Computer wins! Paper covers rock.')
        else:
            print('You win! Rock crushes scissors.')
    elif player.lower() == 'scissors':
        if computer.lower() == 'rock':
            print('Computer wins! Rock crushes scissors.')
        else:
            print('You win! Scissors cuts paper.')
    elif player.lower() == 'paper':
        if computer.lower() == 'scissors':
            print('Computer wins! Scissors cut paper.')
        else:
            print('You win! Paper covers rock.')
    else:
        print('That\'s not a valid option. Please input Rock, Paper or Scissors.')

#player becomes false so loop can continue

    player = False

    computer = option[random.randint(0,2)]






              
