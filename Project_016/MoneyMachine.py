from time import sleep

COIN_VALUE = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}


def processing_time():
    for _ in range(3):
        print(". ", end="")
        sleep(1)
    print()


class MoneyMachine:
    def __init__(self):
        self.transaction_coins = {'penny': 0, 'nickel': 0, 'dime': 0, 'quarter': 0}
        self.cash_store = 0

    def report(self):
        return {'coin bank': self.cash_store}

    def process_transaction(self, price):
        print(f"\n>> Accepted Coins: {', '.join(coin.capitalize() for coin in self.transaction_coins.keys())}")
        print(f">> Price of your drink: {price:.2f}$")

        while True:
            print("-" * 20)
            print(">> Insert number of coins for that type when prompted...")
            for coin in self.transaction_coins.keys():
                coin_count = input(f"{coin}: ").strip().lower()
                if coin_count.isdigit():
                    self.transaction_coins[coin] = int(coin_count)
                else:
                    print(">> Returning all coins", end="")
                    processing_time()
                    print(">> Please try again\n")
                    break
            break

        return self.check_amount(price)

    def check_amount(self, price):
        input_amount = sum(COIN_VALUE[coin] * count for coin, count in self.transaction_coins.items())
        change = input_amount if input_amount < price else (price - input_amount)

        if input_amount < price:
            print(">> You do not have enough coins\n>> Returning all", end="")
            processing_time()
            print(f">> Returned {change}$")
            return False

        self.cash_store += price
        print(">> Returning your change ", end="")
        processing_time()
        print(f">> Returned {abs(change)}$")
        self.transaction_coins = {coin: 0 for coin in self.transaction_coins}
        return True
