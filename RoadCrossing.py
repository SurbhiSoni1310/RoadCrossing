from turtle import Screen
from object import Object
from time import sleep
from cars import Cars
from levels import Level

s = Screen()
s.title("Turtle Crossing Game")
s.setup(width=600, height=600)
s.tracer(0)
toto = Object()
level_board = Level()
s.listen()
s.onkey(toto.move, "Up")
game_is_on = True
car = Cars()
while game_is_on:
    s.update()
    sleep(0.1)
    car.create_car()
    car.movement()
    for j in car.segments:
        if j.distance(toto) < 20:
            game_is_on = False
            level_board.game_over()
    if toto.is_at_finish_line():
        toto.go_to_start()
        level_board.upgrade()
        car.cars_upgrade()

s.exitonclick()
