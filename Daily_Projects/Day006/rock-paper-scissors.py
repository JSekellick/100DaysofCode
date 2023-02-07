rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_imgs = [rock_img, paper_img, scissors_img]

player_choice = input("Rock, Paper, Scissors Battle!!! Choose rock, paper, or scissors: ")
# player_choice = player_choice.lower
computer_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_list)
# print(computer_choice)

if player_choice == "rock" and computer_choice == "paper":
    print(f"Computer chose {computer_choice}, your pethtic rock is smothered away!"), print(game_imgs[0], game_imgs[1])
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Computer chose {computer_choice}, you crushed the scissors with a mighty blow!! YOU WIN!!"), print(game_imgs[0], game_imgs[2])
elif player_choice == "rock" and computer_choice == "rock":
    print(f"Computer chose {computer_choice}, it/'s a draw."), print(game_imgs[0], game_imgs[0])
elif player_choice == "paper" and computer_choice == "rock":
    print(f"Computer chose {computer_choice}, you smothered rock with you paper. Nicely done!!!"), print(game_imgs[1], game_imgs[0])
elif player_choice == "paper" and computer_choice == "paper":
    print(f"Computer chose {computer_choice}, it/'s a draw."), print(game_imgs[1], game_imgs[1])
elif player_choice == "paper" and computer_choice == "scissors":
    print(f"Computer chose {computer_choice}, you are minced into tiny pieces. haha loser"), print(game_imgs[1], game_imgs[2])
elif player_choice == "scissors" and computer_choice == "rock":
    print(f"Computer chose {computer_choice}, you are smashed beyond all recognition. Sucks to be you"), print(game_imgs[2], game_imgs[0])
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Computer chose {computer_choice}, you loose. haha"), print(game_imgs[2], game_imgs[1])
elif player_choice == "scissors" and computer_choice == "scissors":
    print(f"Computer chose {computer_choice}, it/'s a draw."), print(game_imgs[2], game_imgs[2])
else:
    print("That was not a choice, bonehead...")