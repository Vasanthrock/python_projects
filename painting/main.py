###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255)
rgb_colors = []

colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_tuple = (r,g,b)
    rgb_colors.append(new_tuple)
rgb_colors.pop(1)
rgb_colors.pop(0)
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(1,101):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if i % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen=Screen()
screen.exitonclick()

