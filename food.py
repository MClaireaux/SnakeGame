from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # All our food class objects will also be turtles
        self.shape("circle")  # Our food items will all be circles
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Half the turtle width and height
        self.color("white")
        self.speed("fastest")

        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
# All of the above is used from the Trutle super class
#All of this will happened when the food item is called
    def refresh(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
