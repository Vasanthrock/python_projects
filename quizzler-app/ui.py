from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text  = self.canvas.create_text(150,125,width=280,text="something",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,padx=50,pady=50)
        self.right_img=PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img,highlightthickness=0,command=self.true)
        self.right_button.grid(row=2,column=0)
        self.wrong_img=PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img,highlightthickness=0,command=self.false)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text ,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="Nomore questions")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
