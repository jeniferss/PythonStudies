from tkinter import *


def close_project():
    print("Close was choosed")


def save_project():
    print("Save was choosed")


def undo_edit():
    print("Undo was choosed")


def add_file():
    print("Add File was choosed")


root = Tk()

menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)

menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Save", command=save_project)
submenu.add_separator()
submenu.add_command(label="Close", command=close_project)

menu_two = Menu(menu)
menu.add_cascade(label="Edit", menu=menu_two)
menu_two.add_command(label="Undo", command=undo_edit)

toolbar = Frame(root, bg="Pink")

insert_button = Button(toolbar, text="Add  File", command=add_file)
insert_button.pack(side=LEFT, padx=2, pady=3)

print_button = Button(toolbar, text="Print", command=add_file)
print_button.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
