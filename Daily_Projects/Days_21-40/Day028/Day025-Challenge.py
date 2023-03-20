# Replit 100 Days of Code - Day 25 Challenge
# 👉 Day 25 Challenge
# Let's extend Day 24's project and create a health stats generator for a character in a video game.

# Create a subroutine that rolls a dice of any size and returns that number.
# Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
# Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
# Print out the character's health stats.
# Add a loop to give the user the option to generate health stats for another character.
# (We genuinely see this in video games!)

# 🥳 Extra points if you ask for the character's name and double extra points if you use different colors!

import random
characters = {}

# Any sided dice roll
def anySidedDice(sides):
    roll = random.randint(1, sides)
    return roll

# Health Stats Roller
def healthStats():
    player_char = input("Name your character: ")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 8)
    health = dice1 * dice2
    characters[player_char] = health
    print(characters)
    another_char = input("Do you want to make another character?\n 'y' or 'n' ")
    if another_char.lower() == "y":
        healthStats()
    else:
        print("Name   Health")
        for key, value in characters.items():
            print(key + " : " + str(value) + "hp")
healthStats()