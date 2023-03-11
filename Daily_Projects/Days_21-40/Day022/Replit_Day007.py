# tvShow = input("What is your favourite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")

# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#     print("Thank you.")
#     cheese = input("Do you want cheese?")
#     if cheese == "yes":
#         print("You got it.")
#     else:
#         print("No cheese it is.")
# elif order == "pizza":
#     print("Pizza coming up.")
#     toppings = input("Do you want pepperoni on that?")
#     if toppings == "yes":
#         print("We will add pepperoni.")
#     else:
#         print("Your pizza will not have pepperoni.")

# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#   print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#     print("You got it.")
#   else:
#     print("No cheese it is.")
# elif order == "pizza":
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings == "yes":
#     print("We will add pepperoni.")
#   else:
#     print("Your pizza will not have pepperoni.")

# Superfan questionnaire

simpsons = input("Are you a fan of The Simpsons'? (yes or no)")
if simpsons == "yes":
    super_fan = input("Are you super fan? ")
    if super_fan == "yes":
        question01 = input("What is the name of Krusty's daughter? ")
        if question01 == "Sophie" or "sophie":
            print("Well, looks like you know your stuff!")
        else:
            print("You are not a superfan")
    else:
        print("Well, nobody is perfect.")
else:
    print("Well, nobody is perfect.")
