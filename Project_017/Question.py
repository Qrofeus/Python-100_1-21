from random import shuffle


class Question:
    def __init__(self, question: dict):
        self.question_txt = question["question"]
        self.options = question["incorrect_answers"]
        self.options.append(str(question["correct_answer"]))

        shuffle(self.options)

        self.correct_answer = question["correct_answer"]

    def get_question_txt(self):
        return self.question_txt

    def get_question_options(self):
        return self.options

    def get_check_answer(self, selected_option: int):
        return True if self.options[selected_option] == self.correct_answer else False

    def get_option_count(self):
        return len(self.options)
