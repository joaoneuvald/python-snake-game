from turtle import Screen, Turtle           # Imports Screen and Turtle class
import time                                 # Imports time module
from food import Food                       # Imports Food class from the food.py file
from snake import Snake                     # Imports Snake class from the snake.py file
from scoreboard import Scoreboard           # Imports Scoreboard class from the scoreboard.py file

screen = Screen()                           # Instance of the screen class
screen.setup(width=600, height=600)         # Screen resolution
screen.bgcolor('black')                     # Screen background color
screen.title('Snake Game v1.0')             # Title of the screen on Windows
screen.tracer(0)                            # Sets a delay to update a screen

snake = Snake()                             # Instance of the snake class
food = Food()                               # Instance of the food class
scoreboard = Scoreboard()                   # Instance of the scoreboard class

screen.listen()                             # Function to capture the key pressing to the snake movement
screen.onkey(snake.up, "w")                # Binding the 'Up' arrow key with the snake.up function
screen.onkey(snake.down, "s")            # Binding the 'Down' arrow key with the snake.down function
screen.onkey(snake.left, "a")            # Binding the 'Left' arrow key with the snake.left function
screen.onkey(snake.right, "d")          # Binding the 'Right' arrow key with the snake.right function

game_is_on = True                           # Variable to track the game progress
while game_is_on:                           # While loop
    screen.update()                         # Update screen (from screen.tracer())
    time.sleep(0.1)                         # With a 0.1 seconds delay
    snake.move()                            # And move the snake

    if snake.head.distance(food) < 15:      # Checking 'collision' between food and snake
        food.refresh()                      # New food position
        scoreboard.score_up()               # Adding one point to the score
        snake.extend()                      # Adding one segment to the snake

    for segment in snake.segments[1:]:      # Slice of the segments list (parting from the snake head)
        if snake.head.distance(segment) < 10:  # If the distance between the head and a segment is lesser than 10
            snake.reset()               # Resets snake size
            scoreboard.reset()          # Restarts round

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # If the head coordinates encounter the edge of the map
        snake.reset()
        scoreboard.reset()  # # Restarts round


screen.exitonclick()                        # When a click happens in the screen, exit the program

