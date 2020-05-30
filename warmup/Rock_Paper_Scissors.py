import random

moves = ['rock', 'paper', 'scissors']
player_wins = ['paperrock', 'scissorspaper', 'rockscissors']

while True:

    player_move = input("Your move:")
    if player_move == 'q':
        break
    computer_move = random.choice(moves)

    if player_move == computer_move:
        print("Tie Game!")

    elif player_move + computer_move in player_wins:
        print("You won!")

    else:
        print("You lost. ")

    print("The computer played:", computer_move)
    print("You played", player_move)




