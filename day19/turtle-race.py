

from turtle import Screen, Turtle
import random


def createTurtle(tColor, xCoord, yCoord):
    t = Turtle(shape="turtle")
    t.color(tColor)
    t.penup()
    t.goto(x=xCoord, y=yCoord)
    return t

# Setup the Screen
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtleList = []

yLine = -125
for color in colors:
    turtleList.append(createTurtle(color, -230, yLine))
    yLine += 50


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win in this Race?")

isRaceOn = False
if user_bet:
    isRaceOn = True


while isRaceOn:
    for turtle in turtleList:
        if turtle.xcor() >= 230:
            isRaceOn = False
            winner = turtle
            break
        else:
            turtle.forward(random.randint(0, 10))

print(f"{winner.color()[0]} wins the race")
if winner.color()[0] == user_bet:
    print("You win!")
else:
    print("More luck next time")

screen.exitonclick()