from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
sleep_time = 0.20
snake = Snake()
food = Food()
snake.create_snake()
screen.listen()
scoreboard = ScoreBoard()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        if sleep_time > 0.05:
            sleep_time -= 0.005
        scoreboard.increase_score()
        scoreboard.clear()
        scoreboard.update()

    # Detect collision with tail
    for i in range(1, len(snake.places)):
        if snake.segments[0].position() == snake.places[i]:

            scoreboard.reset()
            snake.reset()
            sleep_time = 0.20
            break

    snake.move()
    # Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280:
        scoreboard.reset()
        snake.reset()
        sleep_time = 0.20
    if snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()
        sleep_time = 0.20


screen.exitonclick()