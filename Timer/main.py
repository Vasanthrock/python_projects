from tkinter import PhotoImage
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
time = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(time)
    title.config(text="Timer")
    checkbutton.config(text="")
    canvas.itemconfig(timer,text = "00:00")

    global rep
    rep=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global rep
    rep = rep+1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if rep % 8 ==0:
        count_down(long_sec)
        title.config(text="Long Break", fg=RED)
    elif rep % 2 ==0:
        count_down(short_sec)
        title.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer, text= f"{min}:{sec}")
    if count> 0:
        global time
        time= window.after(1000,count_down,count-1)
    else:
        start()
        mark=""
        div = math.floor(rep/2)
        for i in range(div):
            mark += "✔️"
            Checkbutton.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width=500,height=400)
window.config(padx=100,pady=50,bg=YELLOW)
window.title("Pomodoro")
title = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
title.grid(row=0,column=1)
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,111,image=image)
timer = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold") )
canvas.grid(row=1,column=1)
starting= Button(text="Start", highlightthickness=0,command=start)
starting.grid(row=2,column=0)
checkbutton= Label(bg=YELLOW,fg=GREEN)
checkbutton.grid(row=3,column=1)
Reset= Button(text="Reset", highlightthickness=0, command=reset)
Reset.grid(row=2,column=3)



window.mainloop()