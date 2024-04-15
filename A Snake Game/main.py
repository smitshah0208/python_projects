from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating a snake object from class Snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control a snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()


    # Detect collision with tail
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset_snake()

    # If head collides with any segment in the tail:
        # trigger game over






screen.exitonclick()