from cgitb import text
from sre_parse import State
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20,pady=20)
        self.window.configure(bg=THEME_COLOR)

        self.user_score = Label(text="Score: 0",fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.user_score.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        self.card_question = self.canvas.create_text(150,125, text="Question", fill=THEME_COLOR, width=280, font=("Ariel", 20, "italic"))

        true_img = PhotoImage(file="c:/Users/ANKIT/Desktop/py100/day34/images/true.png")
        false_img = PhotoImage(file="c:/Users/ANKIT/Desktop/py100/day34/images/false.png")

        self.right_button = Button(image=true_img, highlightthickness=0,command=self.is_true)
        self.right_button.grid(row=2,column=0)

        self.wrong_button = Button(image=false_img, highlightthickness=0,command=self.is_false)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.user_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.card_question, text=q_text)
        else:
            self.canvas.itemconfig(self.card_question, text=f"You have finished the Quiz. Your final score: {self.quiz.score - 1}/10")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled") 

    def is_true(self):
            is_right = self.quiz.check_answer("True")
            self.give_feedback(is_right)

    def is_false(self):
            is_right = self.quiz.check_answer("False")
            self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


