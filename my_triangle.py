class Triangle:

    def __init__(self, x_coordinate, y_coordinate, width):
        self.width = width
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate

    def make_triangle(self):
        from turtle import Turtle
        import turtle
        import random

        turtle.colormode(255)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        chosen_color = (red, green, blue)

        my_triangle = Turtle()
        my_triangle.hideturtle()
        my_triangle.penup()
        my_triangle.goto(self.x_coordinate, self.y_coordinate)
        my_triangle.pendown()
        my_triangle.fillcolor(chosen_color)
        my_triangle.begin_fill()

        for _ in range(3):
            my_triangle.forward(self.width)
            my_triangle.left(120)

        my_triangle.end_fill()
