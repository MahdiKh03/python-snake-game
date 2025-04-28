from turtle import Turtle

# Constants
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_length = 3
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(self.snake_length):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(-i * 20, 0)
            self.segments.append(new_turtle)

    def extend(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.segments[-1].position())
        self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
