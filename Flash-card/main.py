BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas as pd
text={}

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df1 = pd.read_csv("./data/french_words.csv")
    text = df1.to_dict(orient="records")
else:
    text = df.to_dict(orient="records")
current_card = {}

def french_word():
    global current_card,flip
    window.after_cancel(flip)
    current_card = random.choice(text)
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word,text=current_card["French"],fill="black")
    canvas.itemconfig(pic, image=old_img)
    flip = window.after(3000,func=flipcard)

def flipcard():
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(pic, image=new_img)
    canvas.itemconfig(word,text=current_card["English"],fill="white")

def known():
    text.remove(current_card)
    data = pd.DataFrame(text)
    data.to_csv("./data/words_to_learn.csv",index=False)
    french_word()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip = window.after(3000,func=flipcard)
canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
new_img = PhotoImage(file="./images/card_back.png")
old_img= PhotoImage(file="./images/card_front.png")
pic = canvas.create_image(400,263,image=old_img)
title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right = PhotoImage(file="./images/right.png")
button = Button(image=right, highlightthickness=0,borderwidth = 0,command=known)
button.grid(row=1,column=0)

wrong = PhotoImage(file="./images/wrong.png")
button = Button(image=wrong, highlightthickness=0,borderwidth=0,command=french_word)
button.grid(row=1,column=1)

french_word()

window.mainloop()