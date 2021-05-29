#A simple password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyssWord, password generator")
n_letters = int(input("How many letters you want in your password?: \n"))
n_symbols = int(input(f"How many symbols would you like?: \n"))
n_numbers = int(input(f"How many numbers would you like?: \n"))

pass_size = n_letters + n_symbols + n_numbers
password = ""

#In order of character addition
for i in range(1, n_letters+1):
    password += random.choice(letters)

for i in range(1, n_symbols+1):
    password += random.choice(symbols)

for i in range(1, n_numbers+1):
    password+=random.choice(numbers)

print(password)



#In random order
pass_list = []

for char in password:
    pass_list.append(char)

password_s = ""
random.shuffle(pass_list)

for item in pass_list:
    password_s += item

print(password_s)



