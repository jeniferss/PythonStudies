from tkinter import *

root = Tk()

label_one = Label(root, text="This is a Tkinter Demo!", bg="Red", fg="White")
label_one.pack(fill=X)

label_two = Label(root, text="This is a Tkinter Demo!", bg="Black", fg="White")
label_two.pack(side=LEFT, fill=Y)

root.mainloop()
