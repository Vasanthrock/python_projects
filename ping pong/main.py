from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
screen.listen()
score = Score()

screen.onkey(l_paddle.up,"Up")
screen.onkey(l_paddle.down,"Down")
screen.onkey(r_paddle.up,"w")
screen.onkey(r_paddle.down,"s")


is_game_on = True
while is_game_on:
    time.sleep(ball.time)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() >380:
        ball.refresh()
        score.l_point()


    if ball.xcor() < -380:
        ball.refresh()
        score.r_point()



screen.exitonclick()