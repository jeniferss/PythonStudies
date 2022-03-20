import turtle
from turtle import Screen, Turtle

import pandas as pd

screen = Screen()
screen.title("Brazil States Game")

on = True

image = "br_map.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv(filepath_or_buffer='br_states.csv', delimiter=';')
states_name = list(states.state)
guessed_states = list()
points = 0

while on:

    if points == len(states_name):
        on = False

    answer = screen.textinput(title=f'{points}/{len(states_name)} States Correct',
                              prompt="What's another state's name?").title()

    if answer == 'Exit':
        with open(file='missing_states.csv', mode='r') as file:
            m_states = file.read()
            print(m_states)
            on = False

    if answer in states_name:
        label = Turtle()
        label.hideturtle()
        label.penup()
        pos_data = states[states.state == answer]
        label.goto(x=float(pos_data.x), y=float(pos_data.y))
        label.write(answer)
        guessed_states.append(answer)
        with open(file='missing_states.csv', mode='w') as missing_states:
            missing_states.write(
                str(list(set(states_name) - set(guessed_states)) + list(set(guessed_states) - set(states_name))))
        points += 1

screen.exitonclick()
