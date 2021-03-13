import time
from turtle import Screen
from paddle import Paddle, POS_LEFT, POS_RIGHT
from ball import Ball
from scoreboard import Scoreboard


SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

class Game():        

    def __init__(self) -> None:
        self.running = True

        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HIGHT)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("PONG")

        self.screen.listen()
        self.screen.onkeypress(self.exitGame, "Escape")

    def exitGame(self):
        print("closing")
        self.running = False

    def run(self):
        scoreboard = Scoreboard()

        pad_l = Paddle(POS_LEFT)
        pad_l.register_listener(self.screen)
        pad_r = Paddle(POS_RIGHT)
        pad_r.register_listener(self.screen)

        ball = Ball()

        while self.running:
            start = time.time()

            ball.move()
            ball.collision(pad_l, pad_r, scoreboard)
            scoreboard.update_score()

            self.screen.update()
            time.sleep(max(1.0/10- (time.time() - start), 0))



game = Game()
game.run()
