from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.__x = 10
        self.__y = 10

    def move(self):
        x = self.xcor() + self.__x
        y = self.ycor() + self.__y
        self.goto(x=x, y=y)

    def bounce_y(self):
        self.__y *= -1

    def bounce_x(self):
        self.__x *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.bounce_x()
