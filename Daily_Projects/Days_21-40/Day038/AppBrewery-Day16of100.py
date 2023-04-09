# import another_module
# print(another_module.another_variable)
# import turtle
# timmy = turtle.Turtle()

""" or write as: 'from turtle import Turtle' """


from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.forward(100)
timmy.color("blue")
timmy.left(77)
timmy.color("darkOrchid")
timmy.forward(100)
timmy.color("LightSeaGreen")
timmy.right(25)
timmy.color("maroon4")
timmy.forward(88)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()