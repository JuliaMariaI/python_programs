#rock-paper-scizzors

import random

def play_game():
    options = ['r','p','s']
    round =[]
    computer_wins =[['r','s'],['p','r'],['s','p']]
    player_wins =[['p','s'],['s','r'],['r','p']]
    tie = [['s','s'], ['r','r'],['p','p']]


    player_choice = input('Please type your choice: r, p, s ')
    round.append(player_choice)
    computer_choice = random.choice(options)
    round.append(computer_choice)
    
    if player_choice in options:
        if round in computer_wins:
            print('You lost')
        elif round in player_wins:
            print('You win')
        else:
            print('tie')
    else:
        print('You mistyped')


play_game()