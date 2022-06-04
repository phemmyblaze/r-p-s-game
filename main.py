# import random


# def play():
#     user = input(
#         "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#     user = user.lower()

#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return "You and the computer have both chosen {}".format(computer)

#     #r > s, s > p, p > r

#     if is_win(user, computer):
#         return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)

#     return "You have chosen {} and the computer has chosen {}. You lost :".format(user, computer)


# def is_win(player, opponent):
#     # return true if the player beats the opponent
#     #r > s, s > p, p > r

#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#         return True
#     return False


# def play_best_of(n):
#     player_wins = 0
#     computer_wins = 0
#     wins_necessary = math.ceil(n / 2)
#     while player_wins < wins_necessary and computer_wins < wins_necessary:
#         result, user, computer = play()
#         # draw
#         if result == 0:
#             print("It's a tie! You and the computer both chose {}\n".format(user))
#         # win
#         elif result == 1:
#             player_wins += 1
#             print("You chose {} and the computer chose {}.You won!\n".format(
#                 user, computer))
#         # lose
#         else:
#             computer_wins += 1
#             print("You chose {} and the computer chose {}.You lost :\n".format(
#                 user, computer))
#         print('\n')

#     if player_wins > computer_wins:
#         print("You win the best of {} game! What a champ".format(n))
#     else:
#         print("Unfortunately, the computer has won the best of {} games !".format(n))


# if __name__ == '__main__':
#     play_best_of(3)

from random import randint

moves = ['rock', 'paper', 'scissors']

while True:
    computer = moves[randint(0, 2)]
    player = input("Rock, paper, scissors? (or end the game)").lower()
    if player == 'end the game':
        print("The game has ended")
        break
    elif player == computer:
        print("This is a Tie")
    elif player == 'rock':
        if computer == 'paper':
            print("You lose! Paper beats Rock")
        else:
            print("You win! Rock beats Scissors")
    elif player == 'paper':
        if computer == 'scissors':
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", "computer")
    elif player == 'scissors':
        if computer == 'rock':
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", "computer")
    else:
        print("Invalid move? check your spelling")
