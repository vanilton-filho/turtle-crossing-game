import random
from turtle import Turtle

CAR = "car.gif"
POLICE_CAR = "police_car.gif"
SPORT_CAR = "sport_car.gif"
FIRE_ENGINE = "fire_engine.gif"
VEHICLES = [CAR, POLICE_CAR, SPORT_CAR, FIRE_ENGINE]


class Vehicle(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.refresh_shape(screen)
        self.penup()

    def move(self):
        self.backward(5)

    def refresh_shape(self, screen):
        new_shape = random.choice(VEHICLES)
        screen.addshape(new_shape)
        self.shape(new_shape)
