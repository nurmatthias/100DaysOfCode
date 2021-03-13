from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.l_score = 0
        self.r_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()

        self.goto(0, 200)
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Ariel", 60, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Ariel", 60, "normal"))
