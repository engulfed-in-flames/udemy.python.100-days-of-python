# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/tutorial/datastructures.html

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock, paper, scissors]

your_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

if not (0 <= your_choice <= 2):
    print("Invalid input. Program Terminated.")
    exit()

print(rps[your_choice])

computer_choice = random.randint(0, 2)
print(f"\nComputer chose: \n{computer_choice}")
print(rps[computer_choice])

if your_choice == computer_choice:
    print("You draw.")

elif your_choice == 0:
    if computer_choice == 1:
        print("You lose.")
    else:
        print("You win.")

elif your_choice == 1:
    if computer_choice == 0:
        print("You win.")
    else:
        print("You lose.")

else:
    if computer_choice == 0:
        print("You lose.")
    else:
        print("You win.")
