class Square:

    def __init__(self, x_coordinate, y_coordinate, width):
        self.width = width
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate

    def make_square(self):
        from turtle import Turtle
        import turtle
        import random

        turtle.colormode(255)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        chosen_color = (red, green, blue)

        my_square = Turtle()
        my_square.hideturtle()
        my_square.penup()
        my_square.goto(self.x_coordinate, self.y_coordinate)
        my_square.pendown()
        my_square.fillcolor(chosen_color)
        my_square.begin_fill()

        for _ in range(4):
            my_square.forward(self.width)
            my_square.left(90)

        my_square.end_fill()
