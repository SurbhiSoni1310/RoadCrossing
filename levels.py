from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 18, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.setposition(-270, 270)
        self.hideturtle()
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def upgrade(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)

