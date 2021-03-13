from turtle import Turtle

POS_LEFT = "LEFT"
POS_RIGHT = "RIGHT"

class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()

        self.position = position

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        if position == POS_LEFT:
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def register_listener(self, screen):
        if self.position == POS_LEFT:
            screen.onkeypress(self.go_up, "w")
            screen.onkeypress(self.go_down, "s")
        else:
            screen.onkeypress(self.go_up, "Up")
            screen.onkeypress(self.go_down, "Down")
