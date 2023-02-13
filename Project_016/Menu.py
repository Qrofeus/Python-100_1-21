from data import coffee_recipes
from MenuItem import MenuItem


class Menu:
    def __init__(self):
        self.drinks_list = {}
        for key in coffee_recipes:
            self.drinks_list[key] = coffee_recipes[key]

    def get_all_drinks(self):
        return self.drinks_list.keys()

    def find_drink(self, drink_name):
        if drink_name not in self.drinks_list:
            return None

        return MenuItem(drink_name=drink_name, drink_dict=coffee_recipes[drink_name])

    def get_menu(self):
        menu_txt = ""
        for drink in self.drinks_list:
            menu_txt += f"{drink}: {self.drinks_list[drink]['price']:.2f}$\n"

        return menu_txt
