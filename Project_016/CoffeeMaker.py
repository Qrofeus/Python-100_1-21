from data import ascii_art
# from MenuItem import MenuItem
from time import sleep

MACHINE_CAPACITY = {
    'milk': 1000,
    'water': 1000,
    'coffee': 500
}


def processing_time(time):
    for _ in range(time):
        print(". ", end="")
        sleep(1)
    print()


class CoffeeMaker:
    def __init__(self):
        print(ascii_art)

        self.ingredients = {key: value for key, value in MACHINE_CAPACITY.items()}
        self.sales_count = 0

        print("Setting up Coffee Machine ", end="")
        processing_time(5)

    def report(self):
        report_dict = {'sales count': self.sales_count}
        for ingredient, amount in self.ingredients.items():
            report_dict[ingredient] = amount
        return report_dict

    def check_resources_available(self, menu_item):
        req_ingredients = menu_item.get_ingredients()
        checks = []
        for i, capacity in self.ingredients.items():
            checks.append(capacity >= req_ingredients[i])
        if all(checks):
            return True
        return False

    def make_coffee(self, menu_item):
        print("\n>> Making your drink\n>> Please Wait ", end="")
        processing_time(5)

        req_ingredients = menu_item.get_ingredients()
        for key, value in self.ingredients.items():
            self.ingredients[key] = value - req_ingredients[key]
        self.sales_count += 1

        print(f">> Please enjoy your {menu_item.get_name().capitalize()}")

    def perform_maintenance(self):
        print("Refilling ingredients ", end="")
        processing_time(3)

        self.ingredients = {key: value for key, value in MACHINE_CAPACITY.items()}
