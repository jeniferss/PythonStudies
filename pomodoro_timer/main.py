import math
import time
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global rep
    rep += 1
    if rep % 8 == 0:
        title_label.config(text='Long Break', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif rep % 2 == 0:
        title_label.config(text='Short Break', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text='Work Time', fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    text = time.strftime("%M:%S", time.gmtime(count))
    canvas.itemconfig(timer_text, text=text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ''
        work_sessions = math.ceil(rep / 2)
        for _ in range(work_sessions):
            marks += '✔'
        checkmarks.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text='reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(text='', fg=GREEN, background=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
