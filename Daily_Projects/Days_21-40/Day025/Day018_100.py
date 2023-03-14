number = 69
guess = 0
counter = 0

print("Make a guess between 1 and 1,000,000")
while number != guess:
    guess = int(input("What is your guess? "))
    counter += 1
    if guess != number:
        if guess < number:
            print("Too low")
        else:
            print("Too high")
        continue
    else:
        counter = str(counter)
        print("You guess correctly with " + counter + " tries.")
    exit()