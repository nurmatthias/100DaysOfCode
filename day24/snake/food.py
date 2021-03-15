import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def hide(self):
        self.hideturtle()

    def show(self):
        self.showturtle()