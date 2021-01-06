from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.goto(0, 275)
        self.color("white")
        self.update()
        self.ht()

    def update(self):
        self.write(arg=f"Your score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

