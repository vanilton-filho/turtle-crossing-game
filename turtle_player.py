from turtle import Turtle


class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto((0, -280))

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.goto((0, -280))
