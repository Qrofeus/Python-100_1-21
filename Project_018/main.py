import turtle
import random

SIZE = 25
DISTANCE = 50
COL_COUNT = 10
ROW_COUNT = 10
COLORS = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
          (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
          (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
          (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


def calculate_position(row_index: int, col_index: int, start_pos: tuple):
    col_pos = start_pos[0] + (col_index * DISTANCE)
    row_pos = start_pos[1] - (row_index * DISTANCE)
    return col_pos, row_pos


def draw_circle(turtle_obj: turtle.Turtle, color_code: tuple[float, float, float]):
    turtle_obj.pendown()
    turtle_obj.dot(SIZE, color_code)
    turtle_obj.penup()


if __name__ == '__main__':
    turtle.colormode(255)

    obj_turtle = turtle.Turtle()
    obj_turtle.speed("fastest")
    obj_turtle.hideturtle()

    col_start = ((COL_COUNT / 2 - 0.5) if COL_COUNT % 2 == 0 else (COL_COUNT // 2)) * DISTANCE
    row_start = ((ROW_COUNT / 2 - 0.5) if ROW_COUNT % 2 == 0 else (ROW_COUNT // 2)) * DISTANCE
    start = (-col_start, row_start)

    obj_turtle.penup()
    obj_turtle.goto(start)

    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            obj_turtle.goto(calculate_position(row, col, start))
            draw_circle(obj_turtle, random.choice(COLORS))

    screen = turtle.Screen()
    screen.exitonclick()
