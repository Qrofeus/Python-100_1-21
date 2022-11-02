from data import coffee_recipes as recipes, ascii_art
from datetime import date
from time import sleep

MILK_CAPACITY = 1000
WATER_CAPACITY = 1000
COFFEE_CAPACITY = 500


class CoffeeMachine:
    def __init__(self):
        self.milk = MILK_CAPACITY
        self.water = WATER_CAPACITY
        self.coffee = COFFEE_CAPACITY
        self.money = 0.00
        self.sales_record = dict.fromkeys(recipes.keys(), 0)

        print(f"Date: {date.today()}")
        print(ascii_art)

    def report(self):
        print(''.join('-' for _ in range(50)))
        print("Available resources:\n")
        print(f"Milk: {self.milk}ml")
        print(f"Water: {self.water}ml")
        print(f"Coffee: {self.milk}g")

        print(f"\nMoney: {self.money:.2f}$")
        print(f"Today's sales -->")
        for recipe, sales in self.sales_record.items():
            print(f"{recipe.capitalize()}: {sales}")

        if self.milk < MILK_CAPACITY or self.coffee < COFFEE_CAPACITY or self.water < WATER_CAPACITY:
            refill = input("\nAsk for a refill?'yes' or 'no'\n>>").strip().lower()
            if refill == 'yes':
                self.refill()

        print("\nClosing report...\n")
        sleep(1.5)

    def refill(self):
        print("Refilling coffee machine ", end='')
        for _ in range(5):
            print('. ', end='')
            sleep(1)
        print()
        self.milk = MILK_CAPACITY
        self.water = WATER_CAPACITY
        self.coffee = COFFEE_CAPACITY

    def check_resources(self, recipe):
        _, milk, water, coffee = recipes[recipe].values()
        if milk > self.milk or water > self.water or coffee > self.coffee:
            print("Insufficient resources for your order...\nPlease check machine 'report'")
            return False
        return True

    def process_transaction(self, recipe):
        cost = recipes[recipe]['price']
        print(f"Your order: {recipe} -> {cost:.2f}$\n")

        coin_value = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}
        print(f"Accepted coins: {', '.join(coin_value.keys())}")
        print("Insert Coins:")
        while True:
            try:
                pennies = int(input("Pennies: ").strip())
                nickels = int(input("Nickels: ").strip())
                dimes = int(input("Dimes: ").strip())
                quarters = int(input("Quarters: ").strip())
                break
            except ValueError:
                print("Invalid input...\nReturning inserted coins ", end='')
                for _ in range(3):
                    print(". ", end='')
                    sleep(0.5)
                print("\nTry again")

        inserted_value = (coin_value['penny'] * pennies) + (coin_value['nickel'] * nickels) + \
                         (coin_value['dime'] * dimes) + (coin_value['quarter'] * quarters)
        if inserted_value < cost:
            print("Not enough coins...")
            print("Returning inserted coins ", end='')
            for _ in range(3):
                print(". ", end='')
                sleep(0.5)
            print(f"\nReturned {inserted_value}$")
            return False

        change = inserted_value - cost
        print(f"To be returned: {change:.2f}$")
        if change > 0:
            print("Returning coins ", end='')
            for _ in range(3):
                print(". ", end='')
                sleep(0.5)
            print(f"\nReturned {change}$")

        self.money += cost
        return True

    def make_coffee(self, recipe):
        _, milk, water, coffee = recipes[recipe].values()

        self.milk -= milk
        self.water -= water
        self.coffee -= coffee

        self.sales_record[recipe] += 1

        print(f"Making your {recipe} ", end='')
        for _ in range(3):
            print(". ", end='')
            sleep(1)
        print(f"\nEnjoy your {recipe}")

    def process_request(self, recipe):
        if self.check_resources(recipe):
            if self.process_transaction(recipe):
                self.make_coffee(recipe)

        print("Closing order...\n")
        sleep(1.5)
        pass

    def get_user_request(self):
        print(''.join('-' for _ in range(50)))
        print("'exit' to close")
        print("Available Recipes --")
        for recipe in recipes:
            print(f"{recipes[recipe]['price']:.2f}$\t{recipe.capitalize()}")

        commands = list(recipes.keys()) + ["report", "exit"]
        while True:
            order = input("\nEnter your order:\n>>").strip().lower()
            if order in commands:
                break
            else:
                print("Invalid input... Try again...")

        if order == "exit":
            print("Closing Coffee Machine...")
            exit(0)

        if order == "report":
            self.report()
            return

        self.process_request(order)
