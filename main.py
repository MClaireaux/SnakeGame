from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # Truns off all real-time animations

game_is_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")  # Up arrow
screen.onkey(snake.down, "Down")  # Down arrow
screen.onkey(snake.left, "Left")  # Left arrow
screen.onkey(snake.right, "Right")  # Right arrow

while game_is_on:
    screen.update()  # Show a new screen after all the pieces moved
    time.sleep(0.1)  # Wait 0.1 second after the 3 segments have moved
    snake.fwd()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        print(scoreboard.score)

    #Detect collision with food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    # If head is within a certain distance of any tail segment, trigger Game Over
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
