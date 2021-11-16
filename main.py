from turtle import Screen
from level_board import LevelBoard
from turtle_player import TurtlePlayer
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("white")
screen.tracer(0)

level_board = LevelBoard()
turtle = TurtlePlayer()
car_manager = CarManager(screen)

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
next_lap = 5
while game_is_on:
    time.sleep(level_board.level_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Comment here
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            level_board.game_over()

    if level_board.next_lap == level_board.level:
        level_board.level_speed = 0.1
        level_board.next_lap += 5

    if turtle.ycor() > 300:
        turtle.reset_position()
        level_board.increase_level()

screen.exitonclick()
