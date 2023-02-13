# Play 3 rounds of rock paper scissor game
# get user choice of rock, paper or scissor
# select random for computer choice
# keep scores for both user and computer
# compare scores at end of play and declare win or draw

from random import choice

choices = ["rock", "paper", "scissor"]


def get_user_input():
    while True:
        user = input("Make your choice: Rock, Paper or Scissor\n>>").strip().lower()
        if user in choices:
            return user
        else:
            print("Invalid choice...")


def get_computer_input():
    return choice(choices)


def compare(user, computer, user_count, computer_count):
    win = ""
    if user == "rock":
        if computer == "paper":
            win = "computer"
        elif computer == "rock":
            win = "draw"
        else:
            win = "user"
    elif user == "paper":
        if computer == "scissor":
            win = "computer"
        elif computer == "paper":
            win = "draw"
        else:
            win = "user"
    else:
        if computer == "rock":
            win = "computer"
        elif computer == "scissor":
            win = "draw"
        else:
            win = "user"

    if win == "computer":
        return ["Computer won this round.", user_count, computer_count + 1]
    elif win == "user":
        return ["You won this round", user_count + 1, computer_count]
    else:
        return ["It was a draw", user_count, computer_count]


if __name__ == '__main__':
    user_wins = 0
    computer_wins = 0
    print("Play 3 rounds of 'Rock, Paper, Scissor'")

    for num in range(3):
        print(f"\n--Round {num+1}--")
        user_choice = get_user_input()
        computer_choice = get_computer_input()
        print(f"Computer chose: {computer_choice}")

        result, user_wins, computer_wins = compare(user_choice, computer_choice, user_wins, computer_wins)
        print(f"Result: {result}")

    print("\nFinal Scores:")
    print(f"Your score: {user_wins}")
    print(f"Computer score: {computer_wins}")
