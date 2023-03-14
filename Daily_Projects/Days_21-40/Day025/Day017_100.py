# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")

# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#     print("Do you want to go up the ladder or down the chute?")
#     direction = input("> ")
#     if direction == "chute":
#         print("Game over!")
#         break
#     elif direction == "ladder":
#         continue
#     else:
#         print("Game over!")
#         exit()
# print("Thanks for playing!")

from getpass import getpass as input
from getpass import getpass as input

# 🪨📄✂️

score1 = 0
score2 = 0

while score1 < 3 or score2 < 3:
    player1 = input("rock, paper or scizzors? (r or p or s)")
    player2 = input("rock, paper or scizzors? (r or p or s)")
    if player1 == "r" and player2 == "r":
        print("You both chose 🪨 It's a tie")
    elif player1 == "r" and player2 == "p":
        print("Player 1 chose 🪨 and Player 2 chose 📄, Player 2 wins!!")
        score2 += 1
    elif player1 == "r" and player2 == "s":
        print("Player 1 chose 🪨 and Player 2 ✂️, Player 1 wins!!!")
        score1 += 1
    elif player1 == "p" and player2 == "r":
        print("Player 1 Wins")
        score1 += 1
    elif player1 == "p" and player2 == "p":
        print("It's a tie")
    elif player1 == "p" and player2 == "s":
        print("Player 2 wins!")
        score2 += 1
    elif player1 == "s" and player2 == "r":
        print("Player 2 wins!")
        score2 += 1
    elif player1 == "s" and player2 == "p":
        print("Player 1 wins!")
        score1 += 1
    elif player1 == "s" and player2 == "s":
        print("It's a tie!")
    print(f"Current score: Player 1 = {score1}, Player 2 = {score2}")
    if score1 == 3 or score2 == 3:
        print("Game Over, Great fun!!")
        exit()

    else:
        print("What?")