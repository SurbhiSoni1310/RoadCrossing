from turtle import Turtle

STEP = 10


class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.go_to_start()
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(STEP)

    def is_at_finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(0, -280)
