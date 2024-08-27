import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars_list = []

screen.listen()
screen.onkeypress(player.go_up,"Up")
scoreboard = Scoreboard()

game_is_on = True
x = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Create a car
    if random.randint(1, 100) > 75 :
        new_car_ = CarManager(x)
        cars_list.append(new_car_)

    #Move Cars
    for car in cars_list:
        car.move_cars_starting()
        #if car passed the line car disappeared from the list
        if car.xcor() < -320:
            cars_list.remove(car)
    #you touch the car game over
    for car in cars_list:
        if player.distance(car) < 17:
            scoreboard.game_over()
            game_is_on = False

    #Detact the car player the celling
    if player.ycor()>290 :
        scoreboard.increase_level()
        player.start_pose()
        x += 1
    for car in cars_list:
        car.move_cars_updated(x)


screen.exitonclick()


