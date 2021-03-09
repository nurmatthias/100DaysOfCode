from turtle import Screen, Turtle
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("brown1", "brown4")

#for _ in range(4):
#    for _ in range(10):
#        timmy.forward(7)
#        timmy.penup()
#        timmy.forward(7)
#        timmy.pendown()
#    timmy.right(90)

sidesToDraw = 3
while sidesToDraw <= 10:
    degree = 360 / sidesToDraw

    timmy.pencolor(random.random(), random.random(), random.random())
    for _ in range(sidesToDraw):
        timmy.forward(100)
        timmy.right(degree)
    
    sidesToDraw += 1




screen = Screen()
screen.exitonclick()
