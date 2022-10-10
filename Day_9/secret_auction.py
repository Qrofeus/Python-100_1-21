# ask for number of auction rounds
# get all bets for that round
# name and bet for each
# no limit for participants in a round
# after round 1 display the highest bet for further rounds
# deny all bets lower than threshold bet from previous round at the time of betting
# get max bet and name after all rounds and declare winner

from os import system


def get_bet(threshold=0):
    while True:
        system('cls')
        print(f"Highest bet last round: {threshold}\nBets below this will not be accepted\n")
        name = input("Your name:\n>>").strip().lower()
        bet = 0
        while True:
            try:
                bet = int(input("Your bet:\n>>").strip())
            except ValueError:
                print("Invalid input... Try again...")
                continue
            break
        if bet <= threshold:
            print("Invalid bet... Try again...")
        else:
            break
    return [name, bet]


if __name__ == '__main__':
    bets = {}
    rounds_count = 1
    while True:
        try:
            rounds_count = int(input("Auction rounds count:\n>>").strip())
        except ValueError:
            print("Invalid input... Try again...")
            continue
        break

    for i in range(rounds_count):
        highest_bet = 0
        try:
            highest_bet = max(bets.values())
        except ValueError:
            pass

        while True:
            new_bet = get_bet(highest_bet)
            bets[new_bet[0]] = new_bet[1]

            system('cls')
            repeat = input("Another participant? 'yes' or 'no'\n>>").strip().lower()
            if not repeat == "yes":
                break

    # Declare winner
    system('cls')
    winner = max(bets, key=bets.get)
    print(f"The winner of the auction is - {winner.capitalize()} - with a value of - {bets[winner]}")
