from getpass import getpass as input
from getpass import getpass as input

# 🪨📄✂️

player1 = input("rock, paper or scizzors? (r or p or s)")
player2 = input("rock, paper or scizzors? (r or p or s)")

if player1 == "r" and player2 == "r":
    print("You both chose 🪨 It's a tie")
elif player1 == "r" and player2 == "p":
    print("Player 1 chose 🪨 and Player 2 chose 📄, Player 2 wins!!")
elif player1 == "r" and player2 == "s":
    print("Player 1 chose 🪨 and Player 2 ✂️, Player 1 wins!!!")
elif player1 == "p" and player2 == "r":
    print("Player 1 Wins")
elif player1 == "p" and player2 == "p":
    print("It's a tie")
elif player1 == "p" and player2 == "s":
    print("Player 2 wins!")
elif player1 == "s" and player2 == "r":
    print("Player 2 wins!")
elif player1 == "s" and player2 == "p":
    print("Player 1 wins!")
elif player1 == "s" and player2 == "s":
    print("It's a tie!")
else:
    print("What?")