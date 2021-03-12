from turtle import Turtle, left, up

MOVE_SPEED = 15
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, snakeSize):
        self.snake = []
        self.speed = MOVE_SPEED

        self.createSnake(snakeSize)
        self.head = self.snake[0]

    def createSnake(self, size):
        for index in range(size):
            self.addSegment(((0-(index*20)), 0))


    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.snake.append(newSegment)

    def extend(self):
        self.addSegment(self.snake[-1].position())
        self.speed += 0.1

    def registerKeyListener(self, screen):
        screen.listen()
        screen.onkeypress(self.up, "Up")
        screen.onkeypress(self.down, "Down")
        screen.onkeypress(self.left, "Left")
        screen.onkeypress(self.right, "Right")

    def hide(self):
        for segment in self.snake:
            segment.hideturtle()

    def show(self):
        for segment in self.snake:
            segment.showturtle()

    def move(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            newX = self.snake[seg_num-1].xcor()
            newY = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
