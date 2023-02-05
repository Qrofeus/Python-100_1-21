# Select one account from data
# show name, follower cont, description, country
# Select second account from data
# show name, description, country
# ask if second has follower count higher or lower than first
# if correctly guessed
# switch second guess with place of first
# get new account from data that was not used previously
# repeat until player guesses wrong
# keep track of score and display at the end

from game_data import data
from game_art import logo
from random import randint
from time import sleep
from os import system


def print_account(index, follower_display):
    print(f"\nName: {data[index]['name']}")
    print(f"Description: {data[index]['description']}")
    print(f"Country: {data[index]['country']}")
    if follower_display == 'yes':
        print(f"\nFollower Count: {data[index]['follower_count']} million")


def higher_lower(a, b):
    print_account(index=a, follower_display='yes')
    print("\n--Vs--")
    print_account(index=b, follower_display='no')

    # Get user guess
    while True:
        guess = input("\nHigher or Lower?\n>>").strip().lower()
        if guess in ['higher', 'lower']:
            break
        else:
            print("Invalid input... Try again...")

    a_followers = data[a]['follower_count']
    b_followers = data[b]['follower_count']
    print(f"\n{data[b]['name']} has {b_followers} million followers")
    sleep(1.5)
    if a_followers == b_followers:
        return True

    answer = "higher" if b_followers > a_followers else "lower"
    if (guess == "higher" and answer == "higher") or (guess == "lower" and answer == "lower"):
        return True
    else:
        return False


def get_account():
    return randint(0, len(data) - 1)


if __name__ == '__main__':
    print(logo)
    completed_deck = []
    score = 0

    # Get first account from data
    account_a = get_account()
    completed_deck.append(account_a)

    while len(completed_deck) < len(data):
        # Get second account from data
        while True:
            account_b = get_account()
            if account_b not in completed_deck:
                completed_deck.append(account_b)
                break

        print(f"\nScore: {score}")
        if higher_lower(account_a, account_b):
            score += 1
            account_a = account_b
            system('cls')
            continue
        else:
            break

    print(f"\nYour final score: {score}")
