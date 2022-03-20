import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

_snake = Snake()
_food = Food()
_score = Score()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MySnakeGame")
screen.tracer(0)

screen.listen()
screen.onkey(fun=_snake.up, key="Up")
screen.onkey(fun=_snake.down, key="Down")
screen.onkey(fun=_snake.left, key="Left")
screen.onkey(fun=_snake.right, key="Right")

on = True
x_limit = screen.window_width() / 2 - 20
y_limit = screen.window_height() / 2 - 20

while on:
    screen.update()
    time.sleep(0.1)
    _snake.move()

    # Food Collision
    if _snake.head.distance(_food) < 15:
        _food.random_location()
        _snake.extend()
        _score.increase_score()

    # Wall Collision
    if _snake.head.xcor() > x_limit or _snake.head.xcor() < -x_limit or _snake.head.ycor() > y_limit or _snake.head.ycor() < -y_limit:
        _score.reset()
        _snake.reset()

    # Self Collision
    for square in _snake.squares[1:]:
        if (_snake.head.distance(square) < 10):
            _score.reset()
            _snake.reset()

screen.exitonclick()
