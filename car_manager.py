from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self,x):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(310,random.randint(-230,230))
        self.inc_x = x


    def move_cars_starting(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - self.inc_x * MOVE_INCREMENT
        self.goto(new_x, self.ycor())

    def move_cars_updated(self,x):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - x * MOVE_INCREMENT
        self.goto(new_x, self.ycor())




