from turtle import Turtle
import random
COLORS = ["blue", "orange", "red", "pink", "purple", "cyan"]


class Cars:
    def __init__(self):
        self.segments = []
        self.car_speed = 10

    def movement(self):
        for seg in self.segments:
            seg.forward(self.car_speed)

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.penup()
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.segments.append(car)

    def cars_upgrade(self):
        self.car_speed += 10
