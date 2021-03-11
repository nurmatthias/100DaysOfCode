from turtle import Screen
from snake import Snake
import time

class Game():

    def __init__(self):
        self.gameRunns = True
        self.gamePaused = True

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("...SnAkE....")   
        self.screen.onkeypress(self.pauseMode, "space")
        self.screen.onkeypress(self.exitGame, "Escape")     


    def pauseMode(self):
        self.gamePaused = not self.gamePaused

    def exitGame(self):
        print("closing")
        self.gameRunns = False


    def play(self):
        snake = Snake(3)
        snake.registerKeyListener(self.screen)

        while self.gameRunns:
            start = time.time()

            if not self.gamePaused:
                snake.move()

            self.screen.update()
            time.sleep(max(1.0/snake.speed - (time.time() - start), 0))


