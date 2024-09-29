RESOURCES: dict[str, dict] = {
    "water": {"amount": 300, "unit": "ml"},
    "milk": {
        "amount": 200,
        "unit": "ml",
    },
    "coffee": {
        "amount": 76,
        "unit": "g",
    },
    "money": {"amount": 2.5, "unit": "$"},
}


COINS: dict[str, float] = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

MENU: dict[str, dict] = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

COMMANDS: list[str] = [
    "report",
    "off",
    "espresso",
    "latte",
    "cappuccino",
    "credit",
]
