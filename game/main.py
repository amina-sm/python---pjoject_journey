# main.py
import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

# Generate random cars
for _ in range(10):
    car_manager.create_car()

game_is_on = True
level = 1
while game_is_on:
    car_manager.move_cars()

    # Check if the player has reached the finish line
    if player.reached_finish_line():
        player.goto(STARTING_POSITION)
        car_manager.increase_speed()
        scoreboard.increase_level()  # Increase the level and update the scoreboard

        # Regenerate cars for the new level
        car_manager.cars.clear()  # Clear existing cars
        for _ in range(10):
            car_manager.create_car()
            
        # Check for collisions with cars
    for car in car_manager.cars:
        if player.is_collision(car):
            game_is_on = False
            scoreboard.game_over()  

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
