from tkinter import *
import random
from random import choice, randint, shuffle
from tkinter import messagebox
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class PasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate a random password with letters, symbols, and numbers
    def generate_password(self):
        # choose 8 to 10 random letters for the password
        password_letters = [random.choice(self.letters) for letter in range(randint(8, 10))]
        # choose 2 to 4 random numbers for the password
        password_numbers = [random.choice(self.numbers) for number in range(randint(2, 4))]
        # choose 2 to 4 random symbols for the password
        password_symbols = [random.choice(self.symbols) for symbol in range(randint(2, 4))]
        # create a list of all numbers, letters, and symbols
        password_list = password_letters + password_symbols + password_numbers
        # shuffle the characters to create the new secure password
        random.shuffle(password_list)
        # remove all spaced from the password
        password = "".join(password_list)
        # copy password to clip board
        pyperclip.copy(password)
        # return password
        return password