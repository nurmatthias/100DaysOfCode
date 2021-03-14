import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

player = Player()
player.register_listener(screen)

car_mgr = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_mgr.tick()

    if car_mgr.collusion(player):
        game_is_on = False
        scoreboard.game_over()

    if player.at_finish_line():
        scoreboard.level_up()
        player.reset_position()
        car_mgr.increase_speed()
    




screen.exitonclick()