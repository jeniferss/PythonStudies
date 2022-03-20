from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.__high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.get_high_score()
        self.__score = 0
        self.goto(x=0, y=270)
        self.show_score()

    def increase_score(self):
        self.__score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Score: {self.__score}  High Score: {self.__high_score}', align='center',
                   font=('Arial', 16, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f'GAME OVER', align='center', font=('Arial', 16, 'normal'))

    def save_high_socre(self):
        with open(file='data.txt', mode='w') as file:
            file.write(f"HIGH SCORE: {self.__high_score}")

    def get_high_score(self):
        with open(file='data.txt') as file:
            high_score = file.read()
            high_score = int(high_score.split(':')[-1]) if high_score else 0
        self.__high_score = high_score

    def reset(self):
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            self.save_high_socre()
        self.__score = 0
        self.show_score()
