from tkinter import *

root = Tk()


def greets():
    print("Hi, there!")


button_one = Button(root, text="Click here!", command=greets)
button_one.pack()

root.mainloop()
