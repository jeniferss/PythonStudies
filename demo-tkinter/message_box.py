import tkinter.messagebox
from tkinter import *

root = Tk()

tkinter.messagebox.showinfo("MessageBox", "This is a MessageBox")

answer = tkinter.messagebox.askquestion("Question One", "Do you like chocolate?")

if answer == 'no':
    print("WHAT?!")
else:
    print("<3")

root.mainloop()
