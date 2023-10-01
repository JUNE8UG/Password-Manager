#Password Generator Project
import random
from random import choice, randint, shuffle


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_letters = [random.choice(letters) for letter in range(randint(8,10))]
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

password_symbols = [random.choice(symbols) for symbol in range(randint(2, 4))]
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)

password_numbers = [random.choice(numbers) for number in range(randint(2, 4))]
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)
print(password_list)

password = "".join(password_list)


print(f"Your password is: {password}")