import turtle
import random
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
