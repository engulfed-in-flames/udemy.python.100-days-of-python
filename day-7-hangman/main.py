# Hangman
import random

stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

words = ["aardvark", "baboon", "camel"]
stage = len(stages)
lives = len(stages) - 1
lives_left = lives
game_over = False

chosen_word = random.choice(words)
answer = chosen_word
placeholder = "_" * len(chosen_word)

while not game_over:
    print(f"Word to guess: {placeholder}")
    guess = input("Guess a letter: ").lower()
    index = chosen_word.find(guess)
    found = chosen_word[index]

    if index != -1:
        placeholder = placeholder[:index] + found + placeholder[index + 1 :]
        chosen_word = chosen_word[:index] + "_" + chosen_word[index + 1 :]
        print(placeholder)
    else:
        lives_left -= 1
        stage -= 1
        print(f"You guessed {found}, that's not in the word. You lose a life")

    if not lives_left:
        game_over = True
        print(f"********** It was '{answer}'! YOU LOSE **********")
    elif placeholder == answer:
        game_over = True
        print(f"********** It was '{answer}'! YOU WIN **********")
    else:
        print(stages[-stage])
        print(f"********** {lives_left}/{lives} LIVES LEFT **********")
