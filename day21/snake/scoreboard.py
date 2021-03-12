from turtle import Turtle


ALIGNMENT = "center"
FONT = "Verdana"
FONT_SIZE = 12


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.score = 0

        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=310)
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, "normal"))
        self.goto(0, -40)
        self.write(f"Your score was {self.score}", align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, "normal"))

    def pause(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME IS PAUSED", align=ALIGNMENT,
                   font=(FONT, FONT_SIZE, "normal"))
