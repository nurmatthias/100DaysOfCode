import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self) -> None:
        self.active_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.start_positions = [int(h) for h in range(-240, 241, 20)]

    def tick(self):
        if random.randint(1, 7) == 1:
            self.add_car()

        for car in self.active_cars:
            car.move(self.move_distance)

        self.remove_cars()


    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT


    def add_car(self):
        self.active_cars.append(Car(random.choice(self.start_positions)))


    def remove_cars(self):
        new_active_cars = []
        for car in self.active_cars:
            if car.xcor() > -320:
                new_active_cars.append(car)
            else:
                car.clear()
                car.hideturtle()
        
        self.active_cars = new_active_cars


    def collusion(self, player):
        for car in self.active_cars:
            coord_diff = car.ycor() - player.ycor()
            if car.distance(player) < 20:
                return True 


class Car(Turtle):

    def __init__(self, start_position=0) -> None:
        super().__init__()

        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()

        self.goto(300, start_position)

    def move(self, move_distance):
        self.backward(move_distance)