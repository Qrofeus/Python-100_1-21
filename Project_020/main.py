from screen_dimensions import SCREEN_HEIGHT, SCREEN_WIDTH, STEP
from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time


def generate_game_screen() -> Screen:
    n_screen = Screen()
    n_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    n_screen.tracer(0)

    n_screen.bgcolor("black")
    n_screen.title("Snake Game")

    n_x_limit = SCREEN_WIDTH // 2 - STEP
    n_y_limit = SCREEN_HEIGHT // 2 - STEP

    return n_screen, n_x_limit, n_y_limit


def wall_collision(snake_obj: Snake, x_max: int, y_max: int):
    if snake_obj.snake_head.xcor() > x_max or snake_obj.snake_head.xcor() < -x_max:
        return True
    if snake_obj.snake_head.ycor() > y_max or snake_obj.snake_head.ycor() < -y_max:
        return True
    return False


if __name__ == '__main__':
    game_is_on = True

    screen, x_limit, y_limit = generate_game_screen()
    snake = Snake(3)
    food = Food()
    scoreboard = ScoreBoard()

    # Keyboard Controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        snake.move()

        # Collision with food
        if snake.snake_head.distance(food) < 1:
            scoreboard.increment_score()
            food.move_to_new_position()
            snake.extend_snake()

        # Collision with wall or tail
        if wall_collision(snake, x_limit, y_limit) or snake.collision_with_tail():
            game_is_on = False
            scoreboard.game_over()

        time.sleep(0.1)
        screen.update()

    screen.exitonclick()
