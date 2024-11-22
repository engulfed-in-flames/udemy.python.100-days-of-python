from classes import MenuItem, Menu, CoffeeMaker, MoneyMachine


def init_coffee_maker() -> CoffeeMaker:
    coffee_maker = CoffeeMaker()

    coffee_maker.add_resource("water", 300, "ml")
    coffee_maker.add_resource("milk", 200, "ml")
    coffee_maker.add_resource("coffee", 76, "g")
    coffee_maker.add_resource("money", 2.5, "4")

    return coffee_maker


def init_money_machine() -> MoneyMachine:
    money_machine = MoneyMachine()

    return money_machine


def init_menu() -> Menu:
    menu = Menu()

    espresso = MenuItem("espresso", 1.5, {"water": 50, "coffee": 18})
    latte = MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24})
    cappuccino = MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})

    menu.add_item(espresso)
    menu.add_item(latte)
    menu.add_item(cappuccino)

    return menu


if __name__ == "__main__":
    coffee_maker = init_coffee_maker()
    money_machine = init_money_machine()
    menu = init_menu()

    is_on = True

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")

        if choice == "off":
            is_on = False
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
