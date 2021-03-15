from turtle import Screen
from game_board import GameBoard
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time


SCREEN_WIDTH = 650
SCREEN_HIGHT = 700
COLLISION_DISTANCE = 18


class Game():

    def __init__(self):
        self.gameRunns = True
        self.gamePaused = True

        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HIGHT)
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
        GameBoard(SCREEN_WIDTH)

        snake = Snake(3)
        snake.registerKeyListener(self.screen)

        food = Food()

        scoreBoard = ScoreBoard()

        while self.gameRunns:
            start = time.time()

            if not self.gamePaused:
                scoreBoard.update_scoreboard()
                snake.show()
                food.show()

                snake.move()

                if self.recognize_collision(snake, food, scoreBoard):
                    snake.hide()
                    food.hide()
                    scoreBoard.game_over()
                    snake.reset()

            else:
                scoreBoard.pause()
                snake.hide()
                food.hide()

            self.screen.update()
            time.sleep(max(1.0/snake.speed - (time.time() - start), 0))

        self.screen.exitonclick()

    def recognize_collision(self, snake, food, scoreBoard):
        
        game_over = False
        if snake.head.distance(food) < COLLISION_DISTANCE:
            snake.extend()
            food.refresh()
            scoreBoard.increase_score()

        if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
            return True

        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < COLLISION_DISTANCE:
                return True
