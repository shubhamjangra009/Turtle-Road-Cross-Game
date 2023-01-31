import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    scoreboard.update_scoreboard()

    # detect collision with car
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect player crosses the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()
