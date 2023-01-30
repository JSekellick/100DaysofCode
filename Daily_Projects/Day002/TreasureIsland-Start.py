<<<<<<< HEAD
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

firstChoice = input(
    "As you begin your journey, your path splits. Do you go left or right? Choose now!!! "
).lower()

if firstChoice == "left":
    secondChoice = input(
        "You chose wisely for you continue on the path until you reach a river. Do you swim or wait? "
    ).lower()
    if secondChoice == "wait":
        thirdChoice = input(
            "You are not a dumb as you look. A smell boatman slowly approaches and offers you a ride accross. You continue on your journey and approach a castle with three doors: red, yellow or blue. Choose!! "
        ).lower()
        if thirdChoice == "yellow":
            print("Well done!! You reached the treasure!!!")
        elif thirdChoice == "red":
            print(
                "A zombie clown was eagerly hiding behind the door. He jumps out and bites. You are dead."
            )
        elif thirdChoice == "blue":
            print("You were eaten by a hoard of ravenous frogs. You are dead.")
        else:
            print(
                "You decided to not choose any of the three doors and died of starvation. You are dead"
            )
    else:
        print(
            "Not a good choice. You drowned trying to cross the raging river. Now your dead."
        )
else:
    print(
        "You are attacked by an angry sentient tree and die a horrible painful death!!!"
    )
=======
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

firstChoice = input(
    "As you begin your journey, your path splits. Do you go left or right? Choose now!!! "
).lower()

if firstChoice == "left":
    secondChoice = input(
        "You chose wisely for you continue on the path until you reach a river. Do you swim or wait? "
    ).lower()
    if secondChoice == "wait":
        thirdChoice = input(
            "You are not a dumb as you look. A smell boatman slowly approaches and offers you a ride accross. You continue on your journey and approach a castle with three doors: red, yellow or blue. Choose!! "
        ).lower()
        if thirdChoice == "yellow":
            print("Well done!! You reached the treasure!!!")
        elif thirdChoice == "red":
            print(
                "A zombie clown was eagerly hiding behind the door. He jumps out and bites. You are dead."
            )
        elif thirdChoice == "blue":
            print("You were eaten by a hoard of ravenous frogs. You are dead.")
        else:
            print(
                "You decided to not choose any of the three doors and died of starvation. You are dead"
            )
    else:
        print(
            "Not a good choice. You drowned trying to cross the raging river. Now your dead."
        )
else:
    print(
        "You are attacked by an angry sentient tree and die a horrible painful death!!!"
    )
>>>>>>> 7ae3e5de56dff183b7d139e0898921c31279b2de
