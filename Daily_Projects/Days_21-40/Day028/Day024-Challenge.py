# Replit 100 Days of Code - Day 24 Challenge
# Create subroutine to roll an X sided die rollDice

import random

print("Infinity Dice 🎲")

sides = int(input("How many sides?: "))
game = True


def rollDice(sides):
    roll = random.randint(1, sides)
    print(f"You rolled {roll}")
while game == True:
    rollDice(sides)
    game_restart = input("Roll again? ")
    if game_restart == "y" or game_restart == "Y":
        rollDice(sides)
    else:
        print("Good bye")
