import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500,400)
input =  screen.textinput(title="Make your bet",prompt="which turtle will win the race? Enter color: ")
colors = ["brown" ,"pink", "black","SeaGreen","red"  ]
y_cor = [-100,-50,0,50,100]
turtles = []
for i in range(5):
    tommy = Turtle(shape="turtle")
    tommy.color(colors[i])
    tommy.penup()
    tommy.goto(-230,y_cor[i])
    turtles.append(tommy)
is_game_on =False

if input:
    is_game_on = True
while is_game_on:
    for tommy in turtles:
        if tommy.xcor() > 220:
            is_game_on =False
            winning_turtle = tommy.pencolor()
            if winning_turtle == input:
                print(f"you've won!, The {winning_turtle} turtle is winner")
            else:
                print(f"you've lost!, The {winning_turtle} turtle is winner")

        rand_turtle =random.choice(turtles)
        rand_turtle.forward(10)











screen.exitonclick()