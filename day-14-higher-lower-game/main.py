import os
from random import choice
from art import logo, vs
from data import data


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def higher_or_lower() -> None:
    print(logo)

    score = 0
    person_comparing = select()

    while True:
        result, person_compared = compare(person_comparing)
        cls()
        print(logo)

        if result:
            score += 1
            person_comparing = person_compared
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        if len(data) == 0:
            print("There is no person to compare. Game is terminated.")
            break


def compare(comparing: object) -> bool:
    compared = select()

    print(f"Compare A: {format_data(comparing)}.")

    print(vs)
    print(f"Against B: {format_data(compared)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = comparing.get("follower_count")
    b_followers = compared.get("follower_count")

    if guess == "a" and a_followers > b_followers:
        return True, compared

    if guess == "b" and a_followers < b_followers:
        return True, compared

    return False, None


def select() -> object:
    selected = choice(data)
    data.pop(data.index(selected))

    return selected


def format_data(person) -> str:
    name = person.get("name")
    description = person.get("description")
    country = person.get("country")

    return f"{name}, a {description}, from {country}"


higher_or_lower()
