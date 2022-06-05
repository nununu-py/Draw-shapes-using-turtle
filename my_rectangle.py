class Rectangle:

    def __init__(self, x_coordinate, y_coordinate, width, height):
        self.height = height
        self.width = width
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate

    def make_rectangle(self):
        from turtle import Turtle
        import turtle
        import random

        turtle.colormode(255)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        chosen_color = (red, green, blue)

        my_rectangle = Turtle()
        my_rectangle.hideturtle()
        my_rectangle.penup()
        my_rectangle.goto(self.x_coordinate, self.y_coordinate)
        my_rectangle.pendown()
        my_rectangle.fillcolor(chosen_color)
        my_rectangle.begin_fill()

        for _ in range(2):
            my_rectangle.forward(self.width)
            my_rectangle.left(90)
            my_rectangle.forward(self.height)
            my_rectangle.left(90)

        my_rectangle.end_fill()
