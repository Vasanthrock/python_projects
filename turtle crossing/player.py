from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def up(self):
            self.forward(MOVE_DISTANCE)

    def down(self):
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)

    def left(self):
            self.setheading(LEFT)
            self.forward(MOVE_DISTANCE)

    def right(self):
            self.setheading(RIGHT)
            self.forward(MOVE_DISTANCE)


