from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [ ]

for question in question_data:
    qu_text= question ["text"]
    qu_answer = question["answer"]
    new_question = Question(qu_text, qu_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("you've completed the quiz")
print(f"Your Final score was : {quiz.current_score}/{quiz.question_number}")


