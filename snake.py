from turtle import Turtle                               # Imports Turtle class
START = [(0, 0), (-20, 0), (-40, 0)]                    # Global variable to track the start position of the snake
MOVE_DISTANCE = 20                                      # Global variable to turn constant the movement distance


class Snake:                                            # Creation of the snake class

    def __init__(self):                                 # Constructor definition
        self.segments = []                              # Segments of the snake
        self.create_snake()                             # Starting snakes creation
        self.move()                                     # Snakes movement
        self.head = self.segments[0]                    # Head of the snake

    def create_snake(self):                             # Snakes creation method
        for _ in START:                                 # For loop
            new_segment = Turtle('square')              # Snake shape = square
            new_segment.color('white')                  # Snake color = white
            new_segment.up()                            # The path of the snake is hidden
            new_segment.goto(_)                         # Default value to start position from START
            self.segments.append(new_segment)           # Adds it to the list of segments

    def move(self):                                     # Snakes movement method
        for seg_num in range(len(self.segments) - 1, 0, -1): # For loop(number of segments, stop condition and step_len)
            new_x = self.segments[seg_num - 1].xcor()   # The new x is the x coordinate of the last segment
            new_y = self.segments[seg_num - 1].ycor()   # The new y is the y coordinate of the last segment
            self.segments[seg_num].goto(new_x, new_y)   # The new position is the union of x and y
        self.segments[0].forward(MOVE_DISTANCE)         # Then move in the direction its heading using the MOVE_DISTANCE

    def up(self):                                       # Up method
        self.head.setheading(90)                        # Make the snake face north

    def down(self):                                     # Down method
        self.head.setheading(270)                       # Make the snake face south

    def left(self):                                     # Left method
        self.head.setheading(180)                       # Make the snake face left

    def right(self):                                    # Right method
        self.head.setheading(0)                         # Make the snake face right

    def add_segment(self, position):                    # Method to create a new segment
        new_segment = Turtle('square')                  # Setting the turtle shape to a square
        new_segment.color('white')                      # Setting the turtle color to white
        new_segment.up()                                # Removing the turtle path
        new_segment.goto(position)                      # Sending the turtle to a specific position
        self.segments.append(new_segment)               # Adds it to the list of segments

    def extend(self):                                   # Method to call the add_segment method
        self.add_segment(self.segments[-1].position())  # Gives the location of the next segment to be inserted

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



