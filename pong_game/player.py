from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.__step = 20
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        y = self.ycor() + self.__step
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - self.__step
        self.goto(self.xcor(), y)
