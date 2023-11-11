from tkinter import *
from PasswordManagerUI import PasswordManagerUI

if __name__ == "__main__":
    # Check if this script is the main module being executed
    # If true, it means the script is not being imported as a module
    
    # Create a Tkinter window
    window = Tk()

    # Create an instance of the PasswordManagerUI class, passing the Tkinter window as a parameter
    app = PasswordManagerUI(window)

    # Start the Tkinter event loop
    window.mainloop()


