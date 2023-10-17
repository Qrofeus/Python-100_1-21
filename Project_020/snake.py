from screen_dimensions import STEP
import turtle

STARTING_POSITION = (0, 0)
LEFT, RIGHT, UP, DOWN = 180, 0, 90, 270


def new_snake_segment() -> turtle.Turtle:
    new_segment = turtle.Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")

    return new_segment


class Snake:
    def __init__(self, body_length: int) -> None:
        self.snake_body = []
        self.snake_length = body_length

        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self) -> None:
        for i in range(self.snake_length):
            new_segment = new_snake_segment()
            new_segment.goto((STARTING_POSITION[0] - i * STEP), STARTING_POSITION[1])

            self.snake_body.append(new_segment)

    def move(self) -> None:
        for i in range(self.snake_length - 1, 0, -1):
            next_position = self.snake_body[i - 1].position()
            self.snake_body[i].goto(next_position)

        self.snake_head.forward(STEP)

    def up(self) -> None:
        if not self.snake_head.heading() == DOWN:
            self.snake_head.setheading(UP)

    def down(self) -> None:
        if not self.snake_head.heading() == UP:
            self.snake_head.setheading(DOWN)

    def left(self) -> None:
        if not self.snake_head.heading() == RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self) -> None:
        if not self.snake_head.heading() == LEFT:
            self.snake_head.setheading(RIGHT)

    def extend_snake(self) -> None:
        new_segment = new_snake_segment()

        # Move segment to position of last segment of current snake
        n_position = self.snake_body[-1].position()
        new_segment.goto(n_position)

        # Add segment to snake body
        self.snake_body.append(new_segment)
        self.snake_length += 1

    def collision_with_tail(self) -> bool:
        for segment in self.snake_body[1:]:
            if any [self.snake_head.distance(segment) < 10]:
                return True
        return False
