from tkinter import messagebox
import json


class PasswordManager:
    def __init__(self):
        # Initialize the data_file attribute with the file name "passwords.json"
        self.data_file = "passwords.json"
        
        # Initialize the passwords attribute as an empty dictionary
        self.passwords = {}

    def save_password(self, website, email, password):
        # Load existing passwords from the file into self.passwords
        self.load_passwords()
        
        # Check if the website already has a saved password
        if website in self.passwords:
            # If the website is found, display a message with the associated email and password
            messagebox.showinfo(title=website,
                                message=f"Email: {self.passwords[website]['email']}, Password: {self.passwords[website]['password']}")
        
        else:
            # If the website is not found, save the provided email and password for the website
            self.passwords[website] = {'email': email, 'password': password}

            # Save the updated passwords to the file
            self.save_passwords()

            # Display a success message
            messagebox.showinfo(
                title="Success!",
                message="Password Saved Successfully!"
            )
            
    # function that puts data from the password data into json format
    def load_passwords(self):
        try:
            #This line attempts to open a file specified by self.data_file in read mode ("r"). 
            # The with statement is used here to ensure that the file is properly closed after reading,
            # even if an error occurs during the operation.
            with open(self.data_file, "r") as password_data:
                # uses the json.load function to deserialize the contents of the opened file (password_data).
                # The deserialized data is then assigned to self.passwords.
                self.passwords = json.load(password_data)
        # If the specified file is not found (raises a FileNotFoundError), the code within this block is executed.
        except FileNotFoundError:
            # keep the dictionary passwords empty if file is not found
            self.passwords = {}

    # function that adds passwords to the password data file
    def save_passwords(self):
        
        # Open the file specified by self.data_file in write mode ("w")
        with open(self.data_file, "w") as password_file:
            # Use json.dump to serialize and write self.passwords to the file
            # The indent=4 argument adds indentation for better readability
            json.dump(self.passwords, password_file, indent=4)
