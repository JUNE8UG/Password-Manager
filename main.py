from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

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
    password_entry.delete(0, END)
    password_entry.insert(END, string=f"{password}")
    # copy password into clip board
    pyperclip.copy(password)
    messagebox.showinfo(title="Copied to Clip Board", message="Copied to clipboard!")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search(website):
    print("Searching ...")
    try:
        with open ("passwords.json", "r") as password_data:
            # reading old data
            website_data = json.load(password_data)
            if website in website_data:
                email = website_data[website]["email"]
                password = website_data[website]["password"]
                # updating old data with new data
                messagebox.showinfo(title=website, message=f"Email: {email}, Password: {password}")
            else:
                raise KeyError

    except KeyError:
        print("no website data found")
        messagebox.showinfo(title="Error", message=f"No details for {website} exists")

    except FileNotFoundError:
        print("creating new json file")
        messagebox.showinfo(title="Error", message=f"Password File Doesn't Exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        oops = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        return

    verify = messagebox.askokcancel(title=website, message= f"These are the details entered: \nEmail: {email} "
                                    f"\nPassword: {password} \n Is it okay to save?")

    # if
    if verify:
        try:
            # open up the passwords.txt file
            with open("passwords.json", "r") as password_file:
                #password_data.write(f"{website} | {email} | {password}\n")
                #json.dump(new_data, password_data, indent=4)
                # reading old data
                data = json.load(password_file)
                # updating old data with new data
                data.update(new_data)
                print("Success ", data)

        except FileNotFoundError:
            print("creating new json file")
            with open("passwords.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)

        else:
            with open("passwords.json", "w") as password_file:
                print("writing new data to file ...")
                # saving updated data or creating data for the first time
                json.dump(data, password_file, indent=4)

        finally:
            # wipe all content entered by the user for website and password inputs
            website_entry.delete(0, END)
            password_entry.delete(0, END)


        # display a successful entry notification
        messagebox.showinfo(title="Success!", message="Password Saved Successfully!")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# display the title
window.title("Password Manager")
# adjust padding
window.config(padx=50, pady=50)

# ---------------------------- CANVAS ------------------------------- #
# create a canvas, canvas controls the shape of the window
canvas = Canvas(width=200, height=200)
# create a tomato image using photo image
logo_img = PhotoImage(file="logo.png")
# you need to set the y and x axis of where the image should be on the screen
# you can use roughly half of the screen width and height to center the image
canvas.create_image(100, 100, image=logo_img)
# use grid instead of pack
canvas.grid(column=1, row=0)

# ---------------------------- TEXT LABELS ------------------------------- #
""" Website label """
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

""" Email/User label """
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

""" Password label """
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ---------------------------- INPUT BOXES ------------------------------- #
""" Website input """
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus() # start the user at the website entry

""" Email/User input """
email_user_entry = Entry(width=39)
email_user_entry.grid(column=1, row=2, columnspan=2)
#email_user_entry.insert(0, "johnny0550@icloud.com")

""" Password input """
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# -------------------------- BUTTONS ---------------------------------- #
""" Search Button """
search_button = Button(text="           Search           ", command=lambda: search(website_entry.get()))
search_button.grid(row=1, column=2, columnspan=2)

""" Generate Password Button """
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

""" Add Button """
# reset button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()