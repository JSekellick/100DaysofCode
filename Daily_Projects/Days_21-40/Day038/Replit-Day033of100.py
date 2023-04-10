# Jared Sekellick

import os, time

# myAgenda = []

# while True:
#   item = input("What's next on the Agenda?: ")
#   myAgenda.append(item)
#   print(myAgenda)

# myAgenda = []

# def printList():
#   print() 
#   for item in myAgenda:
#     print(item)
#   print() 

# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = input("What do you want to remove?: ")
#     myAgenda.remove(item)
#   printList()

# Program is not working

# myAgenda = []

# def printList():
#   print() 
#   for item in myAgenda:
#     print(item)
#   print() 

# while True:
#   menu = input("Add or Remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = ("What do you want to remove?: ")
#     if item in myAgenda:
#       myAgenda.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()

# myPartyList = []

# def printList():
#   print() 
#   for item in myPartyList:
#     print(item)
#   print() 

# while True:
#   menu = input("add or remove?:\n")
#   if menu == "add":
#     item = input("Who should I add to the party list?:\n")
#     myPartyList.append(item)
#   elif menu == "remove":
#     item = input("Who should I remove from the party list?:\n")
#     if item in myPartyList:
#       myPartyList.remove(list)
#     else:
#       print(f"{item} was not in the list")
#   printList()

toDoList = ["eat", "punch a nazi", "nap"]

def listPrinter():
    print(f"Here's your todo list:\n")
    for item in toDoList:
        print(item)
    print()
    

def toDoManager():
    listEdit = True
    while listEdit:
        print("To Do List Manager:")
        user_choice = input("Do you wnat to view, add or edit your todo list?\n")
        if user_choice == "view":
            listPrinter()
        elif user_choice == "add":
            new_item = input("What to add?: ")
            toDoList.append(new_item)
            listPrinter()
        elif user_choice == "edit":
            new_item = input("What would you like to remove?: ")
            toDoList.remove(new_item)
            listPrinter()
        elif user_choice == "exit":
            print("Goodbye you magnificent bastard!!")
            break
        else:
            print("What?! That wasn't an option you knucklehead.")
            toDoManager()

start = input("Would you like to open your To Do Manager? yes/no\n")
if start == "yes":
    toDoManager()
else:
    print("Later gator")