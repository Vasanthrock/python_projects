from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-270,250)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Level : {self.score}", align="Left", font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

    def score_increase(self):
        self.score+=1
        self.clear()
        self.update_score()
