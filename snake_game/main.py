from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_increase()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       score.reset()
       snake.reset()

    for segment in snake.snake_count[1:]:
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()






screen.exitonclick()


