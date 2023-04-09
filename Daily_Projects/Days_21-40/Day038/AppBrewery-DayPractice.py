# import another_module
# print(another_module.another_variable)
# import turtle
# timmy = turtle.Turtle()

""" or write as: 'from turtle import Turtle' """


# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color("blue")
# timmy.left(77)
# timmy.color("darkOrchid")
# timmy.forward(100)
# timmy.color("LightSeaGreen")
# timmy.right(25)
# timmy.color("maroon4")
# timmy.forward(88)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import from_csv 
    # fp = open("addresses.csv", "r")
    # pt = from_csv(fp)
    # fp.close()


from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
# print(table)

pokemonTable = PrettyTable()

pokemonTable.add_column("Name", ["Pikachu", "Squirtle", "Charmander"])
pokemonTable.add_column("Type", ["Electric", "Water", "Fire"])

print(pokemonTable.align)
pokemonTable.align = "l"
print(pokemonTable)

