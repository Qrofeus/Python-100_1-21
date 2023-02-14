from random import randint
from Question import Question


def print_horizontal_line(length: int):
    print("-" * length)


class Quiz:
    def __init__(self, question_list: list, game_length: int):
        self.quizlet_set = question_list
        self.quiz_length = game_length

        self.completed_questions = []

    def ask_question(self):
        max_index = len(self.quizlet_set) - 1

        question_number = randint(0, max_index)
        while question_number in self.completed_questions:
            question_number = randint(0, max_index)

        self.completed_questions.append(question_number)
        new_question = Question(self.quizlet_set[question_number])

        print(new_question.get_question_txt())
        for i, option in enumerate(new_question.get_question_options()):
            print(f"{i + 1}. {option}")

        while True:
            print_horizontal_line(30)
            try:
                user_option = int(input(">> Select your option number: ").strip())
                if new_question.get_option_count() >= user_option > 0:
                    break
            except ValueError:
                print('>> Invalid Input...\n>> Try again')

        return new_question.get_check_answer(user_option - 1)
