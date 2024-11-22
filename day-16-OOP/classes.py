from collections.abc import Mapping
from data import COINS


class MenuItem:
    def __init__(
        self,
        name: str,
        cost: float,
        ingredients: Mapping[str, int],
    ) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

    def __eq__(self, value: str) -> bool:
        return self.name == value

    def __str__(self):
        return self.name


class Menu:
    def __init__(self) -> None:
        self.items: list[MenuItem] = []

    def add_item(self, menu_item: MenuItem) -> None:
        self.items.append(menu_item)

    def get_items(self) -> str:
        if len(self.items) == 0:
            raise Exception("I'm sorry. There is no menu available.")

        return "/".join(str(item) for item in self.items)

    def find_drink(self, drink_name: str) -> MenuItem | None:
        for item in self.items:
            if item == drink_name:
                return item


class CoffeeMaker:
    def __init__(self) -> None:
        self.resources: Mapping = {}

    def add_resource(
        self,
        name: str,
        amount: int,
        unit: str,
    ) -> None:
        self.resources[name] = {"amount": amount, "unit": unit}

    def report(self) -> None:
        for resource, data in self.resources.items():
            print(f"{resource.capitalize()}: {data['amount']}{data['unit']}")

    def is_resource_sufficient(self, menu_item: MenuItem) -> bool:
        for ingredient, amount in menu_item.ingredients.items():
            if amount > self.resources[ingredient]["amount"]:
                print(f"Sorry there is not enough {ingredient}.")
                return False

        return True

    def make_coffee(self, order: MenuItem) -> None:
        if self.is_resource_sufficient(order):
            for ingredient, amount in order.ingredients.items():
                self.resources[ingredient]["amount"] -= amount

            print(f"Here is your {order.name}. Enjoy!")


class MoneyMachine:
    def __init__(self) -> None:
        self.money: float = 0

    def report(self) -> None:
        print(f"Money: ${self.money}")

    def process_coins(self) -> float:
        total = 0

        print("Please insert coins.")
        total += float(input("How many quarters?: ")) * COINS["quarters"]
        total += float(input("How many dimes?: ")) * COINS["dimes"]
        total += float(input("How many nickles?: ")) * COINS["nickles"]
        total += float(input("How many pennies?: ")) * COINS["pennies"]

        return round(total, 2)

    def make_payment(self, cost: float) -> bool:
        paid = self.process_coins()
        change = paid - cost

        if change < 0:
            print("Sorry that's not enough money. Money refunded")
            return False
        else:
            change = round(change, 2)
            self.money += cost
            print(f"Here is ${change} dollars in change")
            return True
