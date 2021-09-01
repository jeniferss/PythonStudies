from tkinter import *


class MyButtons:

    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.print_button = Button(frame, text="Click here!", command=self.print_message)
        self.print_button.pack()

        self.exit_button = Button(frame, text="Exit", command=frame.quit)
        self.exit_button.pack(side=LEFT)

    @staticmethod
    def print_message():
        print("Hi, there!")


root = Tk()
buttons = MyButtons(root)
root.mainloop()
