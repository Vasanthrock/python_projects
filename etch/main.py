import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def counter_clock():
    tim.left(10)
def clock_wise():
    tim.right(10)
def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun= move_forwards)
screen.onkey(key="s", fun= move_backwards)
screen.onkey(key="a", fun = counter_clock )
screen.onkey(key="d", fun= clock_wise)
screen.onkey(key="c", fun= clear)


screen.exitonclick()
