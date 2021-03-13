from turtle import Turtle
import random


MOVE_DISTANCE = 20


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.x_movement = 10 * random.choice([-1, 1])
        self.y_movement = 10 * random.choice([-1, 1])

        self.shape("circle")
        self.color("white")
        self.penup()

        new_x = self.xcor() + random.choice([-1, 1])
        new_y = self.ycor() + random.choice([-1, 1])
        self.goto(new_x, new_y)

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.y_movement *= random.choice([-1, 1])

    def collision(self, l_paddle, r_paddle, scoreboard):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

        if self.distance(l_paddle) < 50 and self.xcor() < -320 or self.distance(r_paddle) < 50 and self.xcor() > 320:
            self.bounce_x()

        if self.xcor() < -380: 
            scoreboard.r_score += 1
            self.reset_position()

        if self.xcor() > 380:
            scoreboard.l_score += 1
            self.reset_position()

