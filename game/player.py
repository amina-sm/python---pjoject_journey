
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    def is_collision(self, other_turtle):
        distance = self.distance(other_turtle)
        return distance < 20  # Adjust the value as needed for your game