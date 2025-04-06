from turtle import Turtle,Screen
import pandas as pd
turtle = Turtle()
screen = Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("50_states.csv")
state = df["state"]
empty=[i for i in state]

count=0
t = Turtle()
t.hideturtle()
t.penup()
is_game_on = True
while count != 50:
    if count > 0:
        answer_text = screen.textinput(title=f"{count}/50 States Correct", prompt="What's the another State Name?").title()
    else:
        answer_text = screen.textinput(title="Guess the input" , prompt = "What's the another State Name?").title()
    cor = df[df.state == answer_text]
    if answer_text == "Exit":
        remaining=pd.DataFrame(empty)
        remaining.to_csv("remaining_States.csv")
        break

    if answer_text in empty:
        count+=1
        empty.remove(answer_text)
        t.goto(int(cor.x),int(cor.y))
        t.write(answer_text)


