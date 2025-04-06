import turtle
from turtle import Turtle,Screen
import random

turtle_obj = Turtle()
turtle.colormode(255)
turtle_obj.shape("turtle")

color=["red","green","yellow","pink","blue","SeaGreen","wheat"]

direction = [0 , 90 , 180 , 270 ]

# turtle_obj.pensize(2)
turtle_obj.speed("fastest")

def color1():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return r,g,b

def circle(gap):
    for i in range(int(360/gap)):
        turtle_obj.color(color1())
        turtle_obj.circle(100)
        turtle_obj.setheading(turtle_obj.heading() + gap)
circle(5)



# def walk(steps):
#     for i in range(steps):
#         turtle_obj.color(color1())
#         rand_dir = random.choice(direction)
#         turtle_obj.color(random.choice(color))
#         turtle_obj.forward(50)
#         turtle_obj.setheading(rand_dir)
#
# walk(50)
# def shape(sides):
#     degree = 360/sides
#     turtle_obj.color(random.choice(color))
#
#     for i in range(sides):
#
#         turtle_obj.forward(100)
#         turtle_obj.right(degree)
#
# for i in range(3,10):
#     shape(i)



# def turn():
#     turtle_obj.forward(100)
#     turtle_obj.left(90)
# for i in range(4):
#     turn()
#
# for i in range(15):
#     turtle_obj.pd()
#     turtle_obj.forward(10)
#     turtle_obj.pu()
#     turtle_obj.forward(10)




screen = Screen()
screen.exitonclick()