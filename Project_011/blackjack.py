# Our Blackjack House Rules:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from random import choice
from time import sleep

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def draw_card():
    return choice(CARDS)


def check_valid(cards):
    return True if sum(cards) < 21 else False


def check_blackjack(cards):
    return True if sum(cards) == 21 else False


def check_aces(cards):
    temp_cards = list(cards)
    for card in cards:
        if card == 11:
            temp_cards[temp_cards.index(card)] = 1
        if check_valid(temp_cards):
            return temp_cards
    return cards


if __name__ == '__main__':
    credit = 500

    while credit > 0:
        dealer_cards = []
        player_cards = []
        round_over = False
        current_bet = 0
        while True:
            try:
                print(f"Available credits: {credit}")
                current_bet = int(input("Your bet:\n>>"))
            except ValueError:
                print("Invalid input... Try again...")
                continue
            if current_bet > credit:
                print("You don't have enough credits")
                continue
            else:
                break

        credit -= current_bet
        print(f"You have bet {current_bet}")
        for _ in range(2):
            dealer_cards.append(draw_card())
            player_cards.append(draw_card())

        while True:
            print(f"\nYour Cards: {player_cards}")
            print("Dealer cards: **face-down**")
            hit = input("Do you want to hit? 'yes' or 'no'\n>>").strip().lower()
            if hit == "yes":
                player_cards.append(draw_card())
                if check_blackjack(player_cards):
                    print("You got a blackjack... Congratulations")
                    credit += current_bet * 2
                    round_over = True
                    break
                else:
                    if not check_valid(player_cards):
                        player_cards = check_aces(player_cards)
                    if check_valid(player_cards):
                        continue
                    else:
                        print(f"Your cards: {player_cards}")
                        print("That is a bust... Your card values are over 21...\nDealer wins")
                        round_over = True
                        break
            else:
                break

        if not round_over:
            while True:
                sleep(2)
                print(f"\nYour cards: {player_cards}")
                print(f"Dealer cards: {dealer_cards}")
                if check_blackjack(dealer_cards):
                    print("Dealer wins with a Blackjack")
                    # No need to update round_over variable
                    break
                else:
                    if not check_valid(dealer_cards):
                        dealer_cards = check_aces(dealer_cards)
                    if check_valid(dealer_cards):
                        dealer_cards.append(draw_card())
                    else:
                        print("That is a bust... Dealer card values are over 21...\nYou win")
                        credit += current_bet * 2
                        # No need to update round_over variable
                        break

        cash_out = input(f"Your credits: {credit}\nDo you want to cash out? 'yes' or 'no'\n>>").strip().lower()
        if cash_out == "yes":
            print(f"You have ended play with {credit} credits in hand\nEnjoy your day")
            exit(0)
