MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "pennies" : 0.01,
    "nickles" : 0.05,
    "dimes" : 0.10,
    "quarters" : 0.25
}

money_bank = 0.00
money_inserted = 0.00

def resourceCheck(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry the machine is out of {item}.")
            return False
    return True

def coins_inserted():
    pennies_inserted = input("How many pennies")
    nickles_inserted = input("How many nickles?")
    dimes_inserted = input("How many dimes?")
    quarters_inserted = input("How many quarters?")
    money_inserted = (pennies_inserted * 0.01) + (nickles_inserted * 0.05) + (dimes_inserted * 0.10) + (quarters_inserted * 0.25)
    if money_inserted > user_choice["cost"]:
        refund = round((money_inserted - user_choice["cost"]), 2)
        return f"Here is your change {refund}"
    elif money_inserted < user_choice["cost"]:
        balance = round((user_choice["cost"] - money_inserted), 2)
        return f"You are short {balance}."

# def coins_insert():
#     for coins_in in coins:
#         money_inserted += input(f"How many {coins_in}") * coins[coins_in]
#     if money_inserted > user_choice["cost"]:
#         refund = money_inserted - user_choice["cost"]
#         print(f"Here is your change {refund}")

# def transaction(money_inserted, coffee_cost):
    


def coffeeOrder(coffee_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {coffee_name}. You filthy animal!")


machine_on = True

while machine_on:
    user_choice = input("☕ What would you like? (espresso / latte / cappuccino): ☕\n")
    if user_choice == "off":
        machine_on = False
        print("Machine is shutting down. Good bye")
        break
    if user_choice == "report":
        print(f"Water remaining: {resources['water']}ml")
        print(f"Milk remaining: {resources['milk']}ml")
        print(f"Coffee remaining: {resources['coffee']}ml")
        print(f"Total money: ${money_bank}")
    else:
        drink = MENU[user_choice]
        if resourceCheck(drink["ingredients"]):
            payment = coins_inserted()
            if coins_inserted(payment, drink["cost"]:
                coffeeOrder(user_choice, drink["ingredients"])
            



# order_ingredients = MENU[user_choice]
# print(order_ingredients)

# if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
    
    

# choice_cost = MENU[user_choice]['cost'])


# def resourceCheck(user_choice):
#     for ingr
#     req_water = resources[user_choice]['water'])
#     req_milk = resources[user_choice]['milk'])
#     req_coffee = resources[user_choice]['coffee'])
    