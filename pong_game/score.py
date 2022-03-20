from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__po_score = 0
        self.__pt_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.__pt_score, align="center", font=("Courier", 50, "normal"))
        self.goto(x=100, y=200)
        self.write(self.__po_score, align="center", font=("Courier", 50, "normal"))

    def increase_po_score(self):
        self.__po_score += 1
        self.show_score()

    def increase_pt_score(self):
        self.__pt_score += 1
        self.show_score()
