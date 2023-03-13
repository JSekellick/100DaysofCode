# while True:
#   print("This program is running")
#   print("Aww, I was having a good time 😭")


# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")


# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
# print("Bye!")


# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
# addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
#   print("Bye!")


# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")


guesses = 1
while True:
  lyrics = input("I'm never gunna ____ you up. ")
  if lyrics == "give" or lyrics == "Give":
    print("You got it!")
  else:
    print("Nope! Try again!")
    guesses +=1
  if lyrics == "give":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", guesses, "attempt(s).")