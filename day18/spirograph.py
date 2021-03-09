import turtle as t
import random

timmy = t.Turtle()
timmy.speed("fastest")

def drawSpirograph(sizeOfGap):
    r = 100
    for _ in range(int(360/sizeOfGap)):
        timmy.pencolor(random.random(), random.random(), random.random())
        timmy.circle(r)
        timmy.setheading(timmy.heading() + sizeOfGap)


drawSpirograph(5)

screen = t.Screen()
screen.exitonclick()