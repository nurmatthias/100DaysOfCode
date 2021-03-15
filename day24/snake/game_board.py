from turtle import Turtle

class GameBoard():
    
    def __init__(self, b_width) -> None:
        self.width = b_width
        self.hight = b_width

        boarder = Turtle()
        boarder.penup()
        boarder.color("white")
        boarder.setposition(-300,-300)
        boarder.pendown()
        boarder.pensize(1)
        for _ in range(4):
            boarder.forward(600)
            boarder.left(90)
        boarder.hideturtle()