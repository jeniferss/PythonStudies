import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Racing Game")

user_input = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ["red", "orange", "yellow", "green", "blue", "black"]
y_pos = [-60, -30, 0, 30, 60, 90]
turtles = []

on = True

for index, color in enumerate(colors):
    player = Turtle(shape="turtle")
    player.penup()
    player.goto(x=-230, y=y_pos[index])
    player.color(color)
    turtles.append(player)

while on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            print('You won!') if user_input == turtle.pencolor() else print(
                f'You lose, {turtle.pencolor()} is the winner!')
            on = False
            break
        dist = random.randint(0, 10)
        turtle.forward(dist)

screen.exitonclick()
