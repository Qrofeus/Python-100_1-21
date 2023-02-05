from hangman_art import stages as lives_art
from hangman_words import word_list as words
from random import choice
from os import system
# Global variables
word = ""
play_word = []
lives = 0
game_over = False
guessed_letters = []


def initiate_game():
    global word, lives
    word = choice(words)
    for _ in range(len(word)):
        play_word.append("_")
    lives = 6


def display_screen():
    system('cls')
    print(lives_art[lives])
    print(f"{' '.join(play_word)}")


def get_letter():
    global play_word, lives
    while True:
        guess = input("Type a letter to guess\n>>").strip().lower()[0]
        print(f"You guessed - '{guess}'")
        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'")
            continue
        else:
            break
    if guess in word:
        for i, letter in enumerate(word):
            if guess == letter:
                play_word[i] = letter
    else:
        print(f"Your guess - {guess} - is not in the word")
        lives -= 1
    game_over_check()


def game_over_check():
    global game_over
    if lives == 0:
        game_over = True
        return
    if "".join(play_word) == word:
        game_over = True


if __name__ == '__main__':
    initiate_game()
    while not game_over:
        display_screen()
        get_letter()

    display_screen()
    if lives > 0:
        print("Congratulations you won...")
    else:
        print("Hard luck...\nYou are out of lives")
    print(f"The word was {word}")

