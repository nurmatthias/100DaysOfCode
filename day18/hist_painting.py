import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('day18/image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

t.colormode(255)

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.goto((50*10/2)*-1, (50*10/2)*-1) 

def draw(space, x): 
  for i in range(x): 
    for j in range(x): 
        # dot 
        tim.dot(20, random.choice(rgb_colors)) 
        # distance for another dot 
        tim.forward(space) 

    tim.backward(space*x) 
      
    tim.left(90) 
    tim.forward(space) 
    tim.right(90) 


draw(50, 10)




screen = t.Screen()
screen.exitonclick()