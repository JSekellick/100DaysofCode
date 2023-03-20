# App Brewery Day 012 of 100 Days of Code - Python
# My Code

print("4A 61 72 65 64  53 65 6B 65 6C 6C 69 63 6B ")
print()
# Jared Sekellick

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print("Welcome to...")
from art import logo

print(logo)

# game_over = False
def start_vars():
    player_guess = 0
    player_attempts = 0



secret_number = random.randint(1, 100)

print("I am your host, Mrs. Calcuthinktor")
print()
print("Let's see how quick you & your monkey brain can work")
print()
print(
    "I am conjuring a number in my memory.\nIt is greater than 0 but <= 100.")

print(f"Pssst, the correct answer is {secret_number}")

start_vars()

# Guess tracker
def guess_tracker():
    game_over = False
    player_attempts = 0
    difficulty = input("Would you like to do this the 'easy' way or the 'hard' way?\n")
    if difficulty.lower() == "easy":
        remaining_attempts = 10
        print("You have 10 guesses.")
    elif difficulty.lower() == "hard":
        remaining_attempts = 5
        print("You have 5 guesses.")
    else:
        print("Not a choice, knucklehead")
        return
    while not game_over:
        player_guess = int(input("What number do you guess?\n"))
        player_attempts += 1
        if player_guess == secret_number:
            print(f"You guessed correctly!! Nicely done, monkeybrain.\n Got it in {player_attempts}.")
            game_over = True
        elif player_guess > secret_number:
            print("Too high")
            remaining_attempts -= 1
            print(f"You have {remaining_attempts} guesses remaining.")
        elif player_guess < secret_number:
            print("Too low")
            remaining_attempts -= 1
            print(f"You have {remaining_attempts} guesses remaining.")
        elif player_guess <= 0:
            print("Really? A negative number?")
        elif player_guess > 100:
            print("Um, what about 'between 1 - 100' did you not understand?")
        else:
            print("What? That's not even a choice")
        if remaining_attempts == 0:
            game_over = True
            print("""
╦  ╔═╗╔═╗╔═╗╦═╗
║  ║ ║╚═╗║╣ ╠╦╝
╩═╝╚═╝╚═╝╚═╝╩╚═""")
            print("You failed... Your ex told me you are a loser.")

# secret_number = 42 # Replace with your own secret number
guess_tracker()


def play_again():
    restart = input("Would you like to play again? 'y' or 'n'\n")
    if restart.lower() == "y":
        secret_number = random.randint(1, 100)
        start_vars()
        guess_tracker()
    else:
        print("Later, sucka!!!")

play_again()