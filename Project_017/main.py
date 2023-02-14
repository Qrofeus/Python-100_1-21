from Quiz import Quiz
import QuizletQuestions as QQues
from os import system

difficulties = {'easy': QQues.quizlet_easy, 'medium': QQues.quizlet_medium, 'hard': QQues.quizlet_hard}


def print_horizontal_line(length: int):
    print("-" * length)


def select_difficulty():
    while True:
        print_horizontal_line(30)
        user_difficulty = input(f">> Select your difficulty level [{', '.join(difficulties.keys())}]:\n") \
            .strip().lower()
        if user_difficulty not in difficulties.keys():
            print(">> Invalid input...\n>> Please try again")
            continue

        return difficulties[user_difficulty]


def select_quiz_length(quizlet: list):
    max_length = len(quizlet)

    while True:
        print_horizontal_line(30)
        length = input(f">> Enter number of questions [max={max_length}]:\n").strip()
        if length.isdigit() and int(length) <= max_length:
            return int(length)
        else:
            print(">> Invalid input...\n>> Please try again")
            continue


if __name__ == '__main__':
    quizlet_set = select_difficulty()
    game_length = select_quiz_length(quizlet_set)
    quiz_game = Quiz(quizlet_set, game_length)

    score = 0

    for i in range(game_length):
        system('cls')
        print(f"Question {i+1}:")
        if quiz_game.ask_question():
            score += 1

    system('cls')
    print(f"Your Score:\n{score} / {game_length}")

