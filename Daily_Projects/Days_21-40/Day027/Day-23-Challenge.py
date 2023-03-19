# Replit Day 23 Challenge
# Create a subroutine with both a username and password.
#Create a loop to prompt the user again and again until they put in the correct login information.

username = "david"
password = "whatAmazingHairYouHave"

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "david" and password == "whatAmazingHairYouHave":
            print("Welcome back, loser.")
            break
        else:
            print("Who the hell do you think you are?? Those are the correct username or passowrds")
print("Loser Login System...")
login()