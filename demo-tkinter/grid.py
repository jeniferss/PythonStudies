from tkinter import *

root = Tk()

label_one = Label(root, text="First Name")
label_two = Label(root, text="Last Name")

entry_one = Entry(root)
entry_two = Entry(root)

label_one.grid(row=0, column=0)
label_two.grid(row=1, column=0)

entry_one.grid(row=0, column=1)
entry_two.grid(row=1, column=1)

root.mainloop()
