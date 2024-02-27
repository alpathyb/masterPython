# Password Generator code
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))

# define list for selected items
set_password = []
# add random item from list
for i in range(nr_letters):
    set_password.append(random.choice(letters))

for i in range(nr_numbers):
    set_password.append(random.choice(numbers))

for i in range(nr_symbols):
    set_password.append(random.choice(symbols))

# combine list than turn into string
genPassword = ''.join(map(str,set_password))

# shuffle the list than turn into string
random.shuffle(set_password)
random_genPassword = ''.join(map(str,set_password))

# print output
print(f"Password with normal order {genPassword}")
print(f"Password with random order {random_genPassword}")
