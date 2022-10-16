# select random number from a range
# ask player to guess a number
# for out of range guesses make player try again
# Display four levels of difference in guessing suggestions
# Too low, low, high, too high
# for differences more than quarter of range display "too..." suggestions

from random import randint


def game_setup():
    print("Number Guessing game")
    while True:
        try:
            low = int(input("\nLower margin:\n>>").strip())
            high = int(input("Upper margin:\n>>").strip())
            if low >= high:
                print("Invalid inputs... Try again...")
                continue
            if high - low < 20:
                print("Please try a wider range for the margins...")
                continue
            break
        except ValueError:
            print("Invalid input... Try again...")
    return [low, high]


def game_difficulty():
    difficulties = {'easy': 10, 'hard': 5}
    while True:
        difficulty = input("Select difficulty: 'easy' or 'hard'\n>>").strip().lower()
        if difficulty not in ['easy', 'hard']:
            print("Invalid input... Try again")
            continue
        return difficulties[difficulty]


def classify_guess(number, guess, low, high):
    threshold = (high - low) / 4
    guess_error = number - guess
    if guess_error > 0:
        if guess_error > threshold:
            print("Your guess is TOO LOW for the selected number")
        else:
            print("Your guess is LOWER than the selected number")
    else:
        if abs(guess_error > threshold):
            print("Your guess is TOO HIGH for the selected number")
        else:
            print("Your guess is HIGHER than the selected number")


if __name__ == '__main__':
    range_low, range_high = game_setup()
    lives = game_difficulty()
    game_number = randint(range_low, range_high)

    player_guess = -999999
    while lives > 0:
        print(f"\nYou have {lives} guesses left")
        while True:
            try:
                player_guess = int(input("Guess a number:\n>>").strip())
                break
            except ValueError:
                print("Invalid input... Try again")
                continue
        lives -= 1
        if player_guess == game_number:
            print("Congratulations\nYou guessed the number")
            exit(0)
        classify_guess(game_number, player_guess, range_low, range_high)

    print(f"You have run out of guesses...\nThe number was {game_number}")



