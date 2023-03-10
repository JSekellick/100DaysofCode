def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
         
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    

    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
    else:
        move()