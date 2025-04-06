from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(0.5,0.5)
        self.color("pink")
        self.speed('fastest')
        self.refresh()
    def refresh(self):
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor,y_cor)

