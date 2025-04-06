import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()

screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
screen.onkey(player.left,"Left")
screen.onkey(player.right,"Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 270:
        score.score_increase()
        player.start()
        car.increase_speed()
    car.move()
    car.create_car()
    for i in car.cars:
        if i.distance(player) < 20:
            score.game_over()
            game_is_on = False





screen.exitonclick()
