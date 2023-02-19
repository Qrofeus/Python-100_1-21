import turtle

STEP = 5
ROTATE_ANGLE = 5


def add_note():
    turtle_note = turtle.Turtle()
    turtle_note.penup()
    turtle_note.hideturtle()
    turtle_note.goto(0, -250)
    turtle_note.pendown()
    turtle_note.write("Press 'Escape' to clear drawings", align="center")


if __name__ == '__main__':
    turtle_obj = turtle.Turtle()

    screen = turtle.Screen()
    screen.listen()

    screen.onkey(lambda: turtle_obj.reset(), "Escape")
    screen.onkeypress(lambda: turtle_obj.forward(STEP), "Up")
    screen.onkeypress(lambda: turtle_obj.backward(STEP), "Down")
    screen.onkeypress(lambda: turtle_obj.left(ROTATE_ANGLE), "Left")
    screen.onkeypress(lambda: turtle_obj.right(ROTATE_ANGLE), "Right")

    screen.exitonclick()
