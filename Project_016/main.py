from MoneyMachine import MoneyMachine
from CoffeeMaker import CoffeeMaker
from time import sleep
from Menu import Menu


def processing_time(time):
    for _ in range(time):
        print(". ", end="")
        sleep(1)
    print()


def create_instruction_set(menu_obj):
    instructions = list(menu_obj.get_all_drinks())
    instructions.append("help")
    instructions.append("menu")
    instructions.append("report")
    instructions.append("quit")

    return instructions


def print_instructions(instructions):
    print(f"Available commands:\n{', '.join(i.capitalize() for i in instructions)}")


def print_horizontal_line():
    print("-" * 30)


if __name__ == '__main__':
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    instruction_set = create_instruction_set(menu)
    print(">> Type 'help' to see the list of commands")

    while True:
        print_horizontal_line()
        command = input(">> Type your order: ").strip().lower()

        if command not in instruction_set:
            print(">> Invalid command...\n>> Try again")
            continue

        if command == "quit":
            print("Closing Coffee-Machine ", end="")
            processing_time(3)
            quit(0)

        if command == "help":
            print_instructions(instruction_set)
            continue

        if command == "menu":
            print(menu.get_menu())
            continue

        if command == "report":
            print("Machine Statistics:")
            report_stats = money_machine.report()
            report_stats.update(coffee_maker.report())

            for key, value in report_stats.items():
                print(f"{key.title()}: {value} unit(s)")

            order_repair = input("\nWould you like to order maintenance for the machine? ('y' or 'n')\n") \
                .strip().lower()[0]
            if order_repair == 'y':
                coffee_maker.perform_maintenance()
            continue

        drink_obj = menu.find_drink(command)
        if not coffee_maker.check_resources_available(drink_obj):
            print(">> There aren't enough ingredients to make your drink")
            print(">> Please check 'report' command for more information")
            continue

        if money_machine.process_transaction(drink_obj.get_price()):
            coffee_maker.make_coffee(drink_obj)

        print("\n>> Closing transaction ", end="")
        processing_time(2)
