from turtle import Turtle                                 # Importing Turtle class
import random                                             # Importing random module


class Food(Turtle):                                       # Creating Food class

    def __init__(self):                                   # Constructor from Turtle + Food Unique attributes and methods
        super().__init__()                                # Inheriting attributes and methods from Turtle class
        self.shape('circle')                              # Setting the food shape to a circle
        self.up()                                         # Removing its path
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Modifying its base width and base length
        self.color('blue')                                # Changing its color to blue
        self.speed(0)                                     # Changing its speed to fastest
        random_x = random.randint(-280, 280)              # Creating the x range
        random_y = random.randint(-280, 280)              # Creating the y range
        self.goto(x=random_x, y=random_y)                 # Setting it to start in a determinate position
        self.refresh()                                    # Method to refresh its location

    def refresh(self):                                    # Method to refresh its location
        random_x = random.randint(-280, 280)              # Creating the x range
        random_y = random.randint(-280, 280)              # Creating the y range
        self.goto(x=random_x, y=random_y)                 # Setting it to start in a determinate position
