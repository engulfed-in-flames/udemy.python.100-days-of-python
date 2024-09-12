# Treasure Island

treasure = '''
  *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     ( `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____/__
  *******************************************************************************
'''

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("\nYou're at a crossroad, where do you want to go?")
answer = input("Left or Right: ").strip().lower()

if answer != "left":
    print("You fell into a hole.")
    print("Game Over.")
    exit()

print("\nYou've come to a lake. There is an island in the middle of the lake.")
answer = input("Swim or Wait?: ").strip().lower()

if answer != "wait":
    print("You drowned")
    print("Game Over.")
    exit()

print(
    "\nYou arrive at the island unharmed. There is house with 3 doors. One read, one yellow and one blue."
)
answer = input("Which color do you choose?: ").strip().lower()

if answer == "red":
    print("It's a room full of fire.")
    print("Game Over.")
elif answer == "blue":
    print("It's a room of beasts.")
    print("Game Over.")
elif answer == "yellow":
    print("You found the treasure. You Win!")
    print(treasure)
else:
    print("You got attacked by an angry trout.")
    print("Game Over.")
