FONT = ("Courier", 24, "normal")


# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 14, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))    
        
        
