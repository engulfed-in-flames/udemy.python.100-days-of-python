# There is no Block Scope in Python!

from random import randint


def guessing_number() -> str:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess()


def guess():
    target = randint(1, 100)
    lives = set_difficulty()

    while True:
        player_guess = int(input("Make a guess: "))

        if player_guess > target:
            print("High")
        elif player_guess < target:
            print("Low")
        else:
            print(f"You got it! The answer was {target}")
            break

        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
        print("Guess again.\n")

        if lives <= 0:
            print("You've run out of guesses. You lose.")
            break


def set_difficulty() -> int:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print("\n")

    if difficulty == "easy":
        return 10

    if difficulty == "hard":
        return 5


guessing_number()
