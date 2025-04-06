from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars =[]
        self.create_car()

    def create_car(self):
        random_int = random.randint(0,6)
        if random_int == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.turtlesize(stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed+=MOVE_INCREMENT

