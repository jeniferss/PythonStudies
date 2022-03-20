import json
import random
import string
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------- PASSWORD GENERATOR --------------------------- #
def password_generator():
    ascii_character = list(string.printable)

    letters = ascii_character[10:62]
    numbers = ascii_character[0:10]
    symbols = ascii_character[62:93]

    p_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    p_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    p_symbols = [random.choice(symbols) for i in range(random.randint(4, 4))]

    p_list = [*p_letters, *p_numbers, *p_symbols]
    random.shuffle(p_list)
    _password = ''.join(p_list)
    pyperclip.copy(_password)
    password_entry.delete(0, END)
    password_entry.insert(0, _password)


# ------------------------ SAVE PASSWORD  ----------------------------- #
def save_password():
    website = website_entry.get().strip().title()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not username or not password:
        messagebox.showerror(title='Missing Parameters', message="Please make sure you haven't left any fields empty.")
    else:
        save = messagebox.askokcancel(title="Save",
                                      message=f'These are the details entered: '
                                              f'\nWebsite:  {website.title()}'
                                              f'\nUsername:  {username}'
                                              f'\nPassword:  {password}'
                                              f'\nIt is ok to save?'
                                      )

        if save:

            data_dict = {
                website: {
                    "username": username,
                    "password": password
                }
            }

            data = data_dict

            try:
                with open(file='data.json', mode='r') as file:
                    data = json.load(file)
                    data.update(data_dict)
            except Exception as error:
                print(error)
            finally:
                with open(file='data.json', mode='w') as file:
                    json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
username_label = Label(text="Username:")
password_label = Label(text="Password:")
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=30)
username_entry = Entry(width=30)
password_entry = Entry(width=15)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

website_entry.focus()

button_generate = Button(text="Generate Password", command=password_generator)
button_save = Button(text="Save", width=30, command=save_password)
button_generate.grid(row=3, column=2, sticky="EW")
button_save.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
