from data import RESOURCES, COINS, MENU, COMMANDS


def report() -> None:
    for resource, info in RESOURCES.items():
        name = resource.lower()
        unit = info.get("unit")
        amount = info.get("amount")

        if resource.lower() == "money":
            print(f"{name}: {unit}{amount}")
        else:
            print(f"{name}: {amount}{unit}")


def select_menu() -> tuple[str, str]:
    while True:
        try:
            answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
            command = COMMANDS[COMMANDS.index(answer)]

            if command == "off":
                raise Exception("Program Terminated")
            elif command == "report":
                report()
                continue
            else:
                return command, MENU[command]
        except ValueError:
            raise ValueError("You picked up the wrong menu.")


def check_resources_is_sufficient(ingredients: dict[str, str]) -> None:
    for ingredient, amount in ingredients.items():
        if RESOURCES[ingredient]["amount"] < amount:
            raise ValueError(f"Sorry there is not enough {ingredient}")


def get_ingredients_and_price(menu: dict) -> tuple[dict, float]:
    ingredients = menu.get("ingredients")
    check_resources_is_sufficient(ingredients)

    cost = menu.get("cost")

    return ingredients, cost


def process_coins() -> float:
    print("Please insert coins.")
    total = 0
    total += float(input("How many quarters?: ")) * COINS["quarters"]
    total += float(input("How many dimes?: ")) * COINS["dimes"]
    total += float(input("How many nickles?: ")) * COINS["nickles"]
    total += float(input("How many pennies?: ")) * COINS["pennies"]

    return round(total, 2)


def is_payment_successful(profit: float) -> bool: ...


def deduct_resources(ingredients: dict, profit: float) -> None:
    for ingredient, amount in ingredients.items():
        RESOURCES[ingredient]["amount"] -= amount


def check_transaction(price: float) -> None:
    paid = process_coins()
    change = paid - price

    if change < 0:
        raise ValueError("Sorry that's not enough money. Money refunded")
    elif change > RESOURCES["money"]["amount"]:
        raise ValueError(f"Sorry, we don't have enough change.")
    elif change > 0:
        change = round(change, 2)
        print(f"Here is ${change} dollars in change")

    RESOURCES["money"]["amount"] += price


def make_coffee() -> bool:
    try:
        menu_name, menu_info = select_menu()
        ingredients, price = get_ingredients_and_price(menu_info)

        check_transaction(price)
        deduct_resources(ingredients)

        print(f"Here is your {menu_name}☕. Enjoy!")

        return True

    except ValueError as e:
        print(e)
        return True
    except Exception as e:
        print(e)
        return False


def main() -> None:
    should_continue = True

    while should_continue:
        should_continue = make_coffee()


if __name__ == "__main__":
    main()
