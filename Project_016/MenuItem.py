class MenuItem:
    def __init__(self, drink_name, drink_dict):
        self.drink = drink_name
        self.price = drink_dict['price']
        self.ingredients = {key: value for key, value in drink_dict.items() if key != 'price'}

    def get_name(self):
        return self.drink

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients
