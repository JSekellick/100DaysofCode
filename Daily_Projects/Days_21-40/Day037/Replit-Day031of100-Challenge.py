import emoji

def word_colors(color):
    if color == "red":
        return ("\033[31m")
    elif color == "green":
        return ("\033[32m")
    elif color == "yellow":
        return ("\033[93m")
    elif color == "blue":
        return ("\033[34m")
    elif color == "pink":
        return ("\033[95m")
    elif color == "white":
        return ("\033[0m")
    else:  
        print("\033[0m", end="") # returns to white or default

prev = "PREV"
next = "NEXT"
pause = "PAUSE"





# title = " Music App "
# print(title.center(17, '='))

print("        \033[31m=\033[0m=\033[34m=\033[93m Music App \033[34m=\033[0m=\033[31m=\033[0m\n")

print("\U0001F525\U000025B6 Radio Gaga")
print(f"\033[93m{'Queen' : >9}\033[0m\n")

print("PREV")
print(f"\033[32m{'NEXT' : ^17}\033[0m")
print(f"\033[95m{'PAUSE' : >17}\033[0m\n\n\n")

print(f"{word_colors('white')}{'WELCOME TO':^40}")
print(f"{word_colors('blue')}{'--    ARMBOOK    --':^40}\n")
print(f"{word_colors('yellow')}{'Definitely not a rip off of' : >40}")
print(f"{word_colors('yellow')}{'a certain other social' : >40}")
print(f"{word_colors('yellow')}{'networking site.' : >40}\n")

print(f"{word_colors('red')}{'HONEST.':^40}\n")

print(f"{word_colors('white')}{'Username:':>24}")
print(f"{word_colors('white')}{'Password:':>24}")