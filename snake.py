from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # List of tupples for the initial positions of the 3 squares. This is a constant, written in all caps
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position()) #Gets hold of the position of the last segmentand add segment at this position

    def fwd(self):
        # #When the snake moves, we hit a problem when the first square moves first. When the first square turns, the others keep moving forward
        # #It will make things easier to start by the end. First, the 3rd square goes where the 2nd one is. The 2nd square goes where the 1st is. The 1st square gets a new position.
        for piece_num in range(len(self.body) - 1, 0,-1):  # Loop through pieces of the snake body backward (range(start,stop,step)) !!Remember the stop is not included in range
             new_x=self.body[piece_num-1].xcor()
             new_y=self.body[piece_num-1].ycor()
             self.body[piece_num].goto(x=new_x, y=new_y) #The segment moves to the coordinates of the one after him
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)