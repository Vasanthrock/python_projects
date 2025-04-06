from turtle import Turtle

POSITION = [(0,0) ,(-20,0) ,(-40,0)]
MOVE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_count = []
        self.create_snake()
        self.head = self.snake_count[0]
    def create_snake(self):
        for position in POSITION:
            self.add(position)

    def add(self,position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.goto(position)
        snake.color("white")
        self.snake_count.append(snake)

    def extend(self):
        self.add(self.snake_count[-1].position())

    def reset(self):
        for i in self.snake_count:
            i.goto(1000,100)
        self.snake_count.clear()
        self.create_snake()
        self.head = self.snake_count[0]

    def move(self):
        for segment in range(len(self.snake_count)-1,0,-1):
                new_x = self.snake_count[segment-1].xcor()
                new_y = self.snake_count[segment-1].ycor()
                self.snake_count[segment].goto(new_x , new_y)
        self.head.forward(MOVE)
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

