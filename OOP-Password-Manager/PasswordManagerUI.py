from tkinter import *
from tkinter import messagebox
from PasswordGenerator import PasswordGenerator
from PasswordManager import PasswordManager


class PasswordManagerUI:

    def __init__(self, window):
        # ---------------------------- UI SETUP ------------------------------- #
        # initialize the main window
        self.window = window
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        # ---------------------------- CANVAS ------------------------------- #
        # Create a canvas for the logo
        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file="lock.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0)

        # ---------------------------- TEXT LABELS ------------------------------- #
        # Labels for website
        self.website_label = Label(text="Website:")
        self.website_label.grid(column=0, row=1)
        # Labels for email/username
        self.email_user_label = Label(text="Email/Username:")
        self.email_user_label.grid(column=0, row=2)
        # Labels for password
        self.password_label = Label(text="Password:")
        self.password_label.grid(column=0, row=3)

        # ---------------------------- INPUT BOXES ------------------------------- #
        # Entry widgets for entering website
        self.website_entry = Entry(width=21)
        self.website_entry.grid(column=1, row=1)
        self.website_entry.focus()
        # Entry for widget for email/username 
        self.email_user_entry = Entry(width=39)
        self.email_user_entry.grid(column=1, row=2, columnspan=2)
        # Entry for password
        self.password_entry = Entry(width=21)
        self.password_entry.grid(column=1, row=3)

        # -------------------------- BUTTONS ---------------------------------- #
        # Buttons for search
        self.search_button = Button(text="Search", command=self.search)
        self.search_button.grid(row=1, column=2, columnspan=2)
        # button for generating password
        self.password_button = Button(text="Generate Password", command=self.generate_password)
        self.password_button.grid(column=2, row=3)
        # button for adding new passwords
        self.add_button = Button(text="Add", width=36, command=self.save_password)
        self.add_button.grid(column=1, row=4, columnspan=2)


    # password generator for secure passwords
    def generate_password(self):
        # create an instance of the password generator
        password_generator = PasswordGenerator()
        # generate the password
        password = password_generator.generate_password()
        # This line clears the current content of the password_entry widget.
        self.password_entry.delete(0, END)
        # After clearing the widget, this line inserts the generated password at the end of the widget. 
        self.password_entry.insert(END, password)


    # searching function for retrieving login info if available
    def search(self):
        # obtain the website given by the user
        website = self.website_entry.get()
        if not website:
            return
        # create an instance of the password manager
        password_manager = PasswordManager()
        # oepns the data file and loads passwords as data
        password_manager.load_passwords()
        # the website is in the password manager
        if website in password_manager.passwords:
            # assign the email as the email value from the password data
            email = password_manager.passwords[website]['email']
            # assign the password as the password value from the password data
            password = password_manager.passwords[website]['password']
            # displa the users emaila nd password in the message box
            messagebox.showinfo(title=website, message=f"Email: {email}, Password: {password}")
        # otherwise there is no data for the given website
        else:
            # notify the user
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
    
    
    # function for saving login data as the user enters them
    def save_password(self):
        # Retrieve values from the input fields
        website = self.website_entry.get()
        email = self.email_user_entry.get()
        password = self.password_entry.get()
        
        # Check if any of the fields are empty
        if not website or not email or not password:
            # Display a message if any field is empty and return from the function
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
            return
        
        # Create an instance of the PasswordManager class
        password_manager = PasswordManager()
        
        # Save the entered website, email, and password using the PasswordManager instance
        password_manager.save_password(website, email, password)
        
        # Clear the input fields after saving the password
        self.website_entry.delete(0, END)
        self.password_entry.delete(0, END)
