import turtle
import random

COLORS = ["red", "green", "blue", "cyan", "lime green", "sky blue"]
RACE_COUNT = 10
WIDTH = 500
STEP = 30


def calc_height(total: int):
    return 2 * total * STEP


def draw_finish_line(turtle_obj: turtle.Turtle, x_pos: int, y_pos: int):
    turtle_obj.penup()
    turtle_obj.goto(x_pos, -y_pos)
    turtle_obj.pendown()
    turtle_obj.goto(x_pos, y_pos)


def prep_race_track(y_pos: int):
    prep = turtle.Turtle(visible=False)
    x_pos = WIDTH // 2 - 15
    draw_finish_line(prep, -x_pos, y_pos)
    draw_finish_line(prep, x_pos, y_pos)
    draw_finish_line(prep, x_pos + 5, y_pos)


def add_turtle(turtle_index: int, turtle_color: str, track_start: int, x_pos: int):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    # new_turtle.speed("fastest")
    new_turtle.penup()
    y_pos = -track_start + STEP * turtle_index
    new_turtle.goto(-x_pos, y_pos)

    return new_turtle


def print_score_turtle(total: int):
    new_turtle = turtle.Turtle(visible=False)
    new_turtle.penup()
    y_pos = total // 2 * STEP
    new_turtle.goto(x=0, y=y_pos)
    new_turtle.pendown()
    return new_turtle


def update_score(turtle_obj: turtle.Turtle, scores: dict):
    turtle_obj.clear()
    score_board = '--'.join([f"{racer.title()}:{score:02d}" for racer, score in scores.items()])
    turtle_obj.write(score_board, align="center")


def reset_turtles(turtles_group: list, x_pos: int):
    for turtle_obj in turtles_group:
        turtle_obj.speed("fastest")
        turtle_obj.setx(-x_pos)
        turtle_obj.speed("slow")


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=calc_height(len(COLORS)))

    total_turtles = len(COLORS)

    y_start = int((total_turtles // 2 - 0.5) * STEP)
    x_border = WIDTH // 2 - 20
    prep_race_track(y_pos=y_start)

    turtles = []
    for index, color in enumerate(COLORS):
        turtles.append(add_turtle(index, color, y_start, x_border))
    # for turtle_obj in turtles:
    #     print(turtle_obj.color())

    score_card = {t_color: 0 for t_color in COLORS}
    # print(score_card)
    score_turtle = print_score_turtle(total_turtles)
    for _ in range(RACE_COUNT):
        race_on = True
        update_score(score_turtle, score_card)
        while race_on:
            for turtle_racer in turtles:
                turtle_racer.forward(random.randint(10, 30))
                if turtle_racer.xcor() > x_border:
                    score_card[turtle_racer.color()[0]] += 1
                    race_on = False
                    break
        reset_turtles(turtles, x_border)

    screen.exitonclick()
