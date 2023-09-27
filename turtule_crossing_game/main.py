import time
from turtle import Screen, Turtle
from player import Player
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
screen.onkey(player.move, "Up")
sleep_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(sleep_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for collision in car_manager.all_car:
        if player.distance(collision) < 20:
            game_is_on = False
            player.game_over()

    if player.ycor() > 280:
        player.finish_line()
        scoreboard.increase_score()
        sleep_speed *= 0.9

















screen.exitonclick()