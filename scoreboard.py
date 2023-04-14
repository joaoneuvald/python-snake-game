from turtle import Turtle               # Imports Turtle class
ALIGNMENT = "center"                    # Global variable to determinate the alignment of the .write()
FONT = ("Arial", 18, "normal")          # Global variable to determinate the font of the .write()


class Scoreboard(Turtle):               # Creation of the scoreboard class, inheriting from Turtle class

    def __init__(self):                 # Constructor for Scoreboard class
        super().__init__()              # Inheriting attributes and methods from Turtle class
        self.color("white")             # Setting color to white
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()               # Hiding Turtle
        self.up()                       # Removing its path
        self.score = 0                  # Setting a base attribute for score
        self.goto(x=0, y=270)           # Sending the turtle to a specific location of the screen
        self.update_scoreboard()        # Method that updates the score display

    def update_scoreboard(self):        # Method to write the score again
        self.clear()                    # Clears the last message related to the score in the screen
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)  # Writing
        # configuration

    # def game_over(self):                                        # Game over method
    #    self.goto(0, 0)                                          # Goes back to the center of the screen
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)      # Prints game over

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0

    def score_up(self):                 # Method to keep track of the score
        self.score += 1                 # Adds one point to the score attribute
        self.update_scoreboard()        # Prints the score again







