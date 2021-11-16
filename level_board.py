from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")


class LevelBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto((-220, 250))
        self.level_speed = 0.1
        self.next_lap = 5
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()
        self.level_speed *= 0.9

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
