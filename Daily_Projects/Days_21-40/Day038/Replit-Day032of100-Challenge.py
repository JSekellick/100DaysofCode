# Jared Sekellick

# timetable = ["Computer Science", "Math", "English", "Art", "Sport"]

# print(timetable[0])
# print(timetable[1])
# print(timetable[2])
# print(timetable[3])
# print(timetable[4])


# for i in timetable:
#     print(i, end=", ")

# timetable[4]= "Watch TV"
# print(timetable[0])
# print(timetable[1])
# print(timetable[2])
# print(timetable[3])
# print(timetable[4])

# timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
# for lesson in timetable:
#   print(lesson)


# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
# print(f"The first color is {colors[0]}")

# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
# print(f"The last color is {colors[-1]}")

# grocery_list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
# print(f"The first grocery item to buy is {grocery_list[0]}.")

# greeting_list = ["French", "Spanich", "Russian", "Chinese", "Italian", "Japanese", "German", "Portuguese", "Korean", "Arabic", "Danish", "Swahili", "Dutch", "Greek", "Polish", "Indonesian", "Hindi", "Turkish", "Swedish", "Norwegian"]

import random

French = {'Formal' : 'Bonjour',
          'Informal' : 'Salut',}
Spanish = {'Formal' : 'Hola',
           'Informal' : '¿Qué tal? (What’s up?)',}
Russian = {'Formal' : 'Zdravstvuyte',
           'Informal' : 'Privet',}
Chinese = {'Formal' : 'Nǐn hǎo',
           'Informal': 'Nǐ hǎo',}
Italian = {'Formal' : 'Salve',
           'Informal' : 'Ciao',}
Japanese = {'Formal' : 'Konnichiwa',
            'Informal' : 'Yā, Yō',}
German = {'Formal' : 'Guten Tag',
          'Informal' : 'Hallo, Hi',}
Portuguese = {'Formal' : 'Olá',
              'Informal' : 'Oi',}
Korean = {'Formal' : 'Anyoung haseyo',
          'Informal' : 'Anyoung',}
Arabic = {'Formal' : 'Asalaam alaikum (Peace be upon you)',
          'Informal' : 'Ahlan',}
Danish = {'Formal' : 'Goddag',
          'Informal' : 'Hej, Halløj'}
Swahili = {'Formal' : 'Shikamoo',
           'Informal' : 'Habari, Hujambo',}
Dutch = {'Formal' : 'Goedendag',
         'Informal' : 'Hoi, Hallo',}
Greek = {'Formal' : 'Yassas',
         'Informal' : 'Yassou',}
Polish = {'Formal' : 'Dzień dobry',
          'Informal' : 'Cześć, Witaj',}
Indonesian = {'Formal' : 'Selamat siang',
              'Informal' : 'Halo',}
Hindi = {'Formal' : 'Namaste, Namaskar',
         'Informal' : 'Hai, Helo',}
Turkish = {'Formal' : 'Merhaba',
           'Informal' : 'Selam',}
Hebrew = {'Formal' : 'Shalom',
          'Informal' : 'Hey',}
Swedish = {'Formal' : 'God dag',
           'Informal' : 'Hej, Tjena',}
Norwegian = {'Formal' : 'God dag',
             'Informal' : 'Hei',}

greeting_list = [French, Spanish, Russian, Chinese, Italian, Japanese,
                 German, Portuguese, Korean, Arabic, Danish, Swahili, 
                 Dutch, Greek, Polish, Indonesian, Hindi, Turkish,
                 Swedish, Norwegian]

list_items = len(greeting_list) - 1
# print(len(greeting_list))

list_random = random.randint(0, list_items)
chosen_dict = greeting_list[list_random]

print(f"Formal greeting: {greeting_list[list_random]['Formal']}")
print(f"Informal greeting: {greeting_list[list_random]['Informal']}")

# random.randint(0, (len(greeting_list) + 1)