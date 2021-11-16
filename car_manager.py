import random

from vehicle import Vehicle


class CarManager:

    def __init__(self, screen):
        super().__init__()
        self.all_cars = []
        self.screen = screen

    def create_car(self):
        if random.randint(0, 6) == 1:
            y_cord = random.randint(-250, 250)
            new_car = Vehicle(self.screen)
            new_car.goto((300, y_cord))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.move()
