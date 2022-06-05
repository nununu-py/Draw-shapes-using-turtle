from my_rectangle import Rectangle
from my_triangle import Triangle
from my_square import Square
from turtle import Screen

screen = Screen()
screen.setup(width=700, height=700)

star_drawing = False

while not star_drawing:

    ask_user = screen.textinput(title="What do you want", prompt="Draw a (Rectangle, Square, Triangle) / (exit)").\
        lower()

    if ask_user == "rectangle":
        setX_position = screen.textinput(title="Set x coordinate for your rectangle",
                                         prompt="Pleas add a integer")
        setY_position = screen.textinput(title="Set y coordinate for your rectangle",
                                         prompt="Pleas add a integer")
        set_width = screen.textinput(title="Set width of your rectangle", prompt="Please add a integer")
        set_height = screen.textinput(title="Set height of your rectangle", prompt="Please add a integer")

        rectangle = Rectangle(x_coordinate=int(setX_position), y_coordinate=int(setY_position),
                              width=int(set_width), height=int(set_height))
        rectangle.make_rectangle()

    elif ask_user == "square":
        setX_position = screen.textinput(title="Set x coordinate for your square",
                                         prompt="Pleas add a integer")
        setY_position = screen.textinput(title="Set y coordinate for your square",
                                         prompt="Pleas add a integer")
        set_width = screen.textinput(title="Set width of your square", prompt="Please add a integer")

        square = Square(x_coordinate=int(setX_position), y_coordinate=int(setY_position), width=int(set_width))
        square.make_square()

    elif ask_user == "triangle":
        setX_position = screen.textinput(title="Set x coordinate for your triangle",
                                         prompt="Pleas add a integer")
        setY_position = screen.textinput(title="Set y coordinate for your triangle",
                                         prompt="Pleas add a integer")
        set_width = screen.textinput(title="Set width of your triangle", prompt="Please add a integer")

        triangle = Triangle(x_coordinate=int(setX_position), y_coordinate=int(setY_position), width=int(set_width))
        triangle.make_triangle()

    else:

        star_drawing = True

screen.exitonclick()
