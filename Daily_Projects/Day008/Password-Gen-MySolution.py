#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password1 = random.choices(letters, k=nr_letters)
password2 = random.choices(numbers, k=nr_numbers)
password3 = random.choices(symbols, k=nr_symbols)

combined_password = (password1 + password2 + password3)
# print(password1 + password2 + password3)
# print(combined_password)
shuffled_password = combined_password

join = ''.join(combined_password)
print(join)

# join1 = ''.join(password1)
# join2 = ''.join(password2)
# join3 = ''.join(password3)

# combined = (join1 + join2 + join3)
# print(join1 + join2 + join3)
# print(combined)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


random.shuffle(shuffled_password)
joined_shuffled = ''.join(shuffled_password)

print(joined_shuffled)