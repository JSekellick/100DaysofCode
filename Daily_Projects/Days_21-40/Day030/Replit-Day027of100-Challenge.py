# Replit Day 027 of 100 Days of Code - Python
# My Code

# print("4A 61 72 65 64  53 65 6B 65 6C 6C 69 63 6B ")
# print()
# Jared Sekellick

import random, os, time

print("Character Builder")

# Character name and type
# def name_char():
#     char_name = input("Name Your Hero:\n")
#     char_type = input("Character type (Hooman, Elf, Wizard or Orc):\n")
#     print(f"Welcome {char_name} the {char_type}.")
#     time.sleep(1)
    
# name_char()


# # Health stat generator
# def health_char_start():
#     health_stat01 = random.randint(1 , 6)
#     health_stat02 = random.randint(1, 12)
#     health = ((( health_stat01 * health_stat02 ) / 2) + 10)
#     print(f"Your health is: {health}")
#     time.sleep(1)

# health_char_start()

# # Strength generator
# def strength_char_start():
#     strength_start01 = random.randint(1 , 6)
#     strength_start02 = random.randint(1, 12)
#     strength = ((( strength_start01 * strength_start02 ) / 2) + 10)
#     print(f"Your strength is: {strength}.")
#     time.sleep(1)
    
# strength_char_start()



# Below is the provided code as the answer
import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

while True:
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")