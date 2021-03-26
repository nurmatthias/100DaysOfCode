from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Ui():

    def __init__(self, quiz_brain: QuizBrain) -> None:

        self.quiz = quiz_brain

        self.app = Tk()
        self.app.title("Quizzler")
        self.app.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.lbl_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,
                             bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(
            150, 125, width=280, text="Frage", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(50, 50))

        true_image = PhotoImage(file="day34/images/true.png")
        self.btn_true = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.btn_true.image = true_image
        self.btn_true.grid(column=0, row=2, pady=(10, 0))

        false_image = PhotoImage(file="day34/images/false.png")
        self.btn_false = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.btn_false.image = false_image
        self.btn_false.grid(column=1, row=2, pady=(10, 0))

        self.get_next_question()

    def render(self):
        self.app.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.lbl_score.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.app.after(1000, self.get_next_question)