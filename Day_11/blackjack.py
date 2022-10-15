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

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def get_card():
    return choice(CARDS)


def check_valid(cards):
    return True if sum(cards) <= 21 else False


def check_blackjack(cards):
    return True if sum(cards) == 21 else False


def check_aces(cards):
    new_cards = []
    for card in cards:
        if card == 11:
            new_cards.append(1)
        else:
            new_cards.append(card)
        if check_valid(new_cards):
            return new_cards


if __name__ == '__main__':
    dealer_cards = []
    player_cards = []
