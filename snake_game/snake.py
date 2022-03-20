from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.__initial_segments = 3
        self.squares = []
        self.__step = 20
        self.__initial_positions = [(index * -20, 0) for index in range(0, self.__initial_segments)]
        self.initialize_snake()
        self.head = self.squares[0]

    def initialize_snake(self):
        for position in self.__initial_positions:
            self.add_square(position=position)

    def add_square(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def extend(self):
        self.add_square(position=self.squares[-1].position())

    def move(self):
        for index in range(len(self.squares) - 1, 0, -1):
            next_x = self.squares[index - 1].xcor()
            next_y = self.squares[index - 1].ycor()
            self.squares[index].goto(x=next_x, y=next_y)
        self.head.forward(self.__step)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for square in self.squares:
            square.goto(x=1000, y=1000)
        self.squares.clear()
        self.initialize_snake()
        self.head = self.squares[0]
