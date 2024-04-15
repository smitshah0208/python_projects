import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard =Scoreboard()



screen.listen()
screen.onkey(fun=player.go_up, key ="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()





