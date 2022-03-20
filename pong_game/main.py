from turtle import Screen
from time import sleep

from player import Player
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("MyPongGame")
screen.tracer(0)

on = True

score = Score()

player_one = Player(position=(350, 0))
player_two = Player(position=(-350, 0))
ball = Ball()

screen.listen()
screen.onkey(fun=player_one.up, key="Up")
screen.onkey(fun=player_one.down, key="Down")
screen.onkey(fun=player_two.up, key="w")
screen.onkey(fun=player_two.down, key="s")

while on:
    sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Collision with bottom and up wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with players
    if ball.distance(player_one) < 58 and ball.xcor() > 320 or ball.distance(player_two) < 58 and ball.xcor() < -320:
        ball.bounce_x()

    # Missed ball - Player One
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_pt_score()

    # Missed ball - Player Two
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_po_score()

screen.exitonclick()
